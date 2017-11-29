import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from apps.tracking import models


class DeviceType(DjangoObjectType):
    class Meta:
        model = models.Device


class PositionType(DjangoObjectType):
    class Meta:
        model = models.Position


class Query(ObjectType):
    device = category = graphene.Field(DeviceType, id=graphene.Int(), serial_number=graphene.String())
    devices = graphene.List(DeviceType)
    positions = graphene.List(PositionType, device_id=graphene.Int())

    def resolve_device(self, info, **kwargs):
        id = kwargs.get('id')
        serial_number = kwargs.get('serial_number')

        if id is not None:
            return models.Device.objects.get(id=id)

        if serial_number is not None:
            return models.Device.objects.get(serial_number=serial_number)

        return None

    def resolve_devices(self, info, **kwargs):
        filters = {}
        if info.context.user.is_authenticated():
            filters['user_id'] = info.context.user
        else:
            models.Device.objects.none()

        return models.Device.objects.filter(**filters)

    def resolve_positions(self, info, **kwargs):
        filters = {}
        if info.context.user.is_authenticated():
            filters['device__user_id'] = info.context.user
        else:
            return models.Position.objects.none()

        device_id = kwargs.get('device_id')
        if device_id is not None:
            filters['device_id'] = device_id

        return models.Position.objects.filter(**filters)
