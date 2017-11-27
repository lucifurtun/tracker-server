import graphene
from graphene_django import DjangoObjectType

from apps.tracking import models, utils


class DeviceType(DjangoObjectType):
    class Meta:
        model = models.Device
        # interfaces = (graphene.relay.Node,)
        # only_fields = ('id', 'pk', 'serial_number')


class PositionType(DjangoObjectType):
    class Meta:
        model = models.Position


class Query(object):
    device = category = graphene.Field(DeviceType, id=graphene.Int(), serial_number=graphene.String())
    devices = graphene.List(DeviceType)
    positions = graphene.List(PositionType)

    def resolve_device(self, info, **kwargs):
        id = kwargs.get('id')
        serial_number = kwargs.get('serial_number')

        if id is not None:
            return models.Device.objects.get(id=id)

        if serial_number is not None:
            return models.Device.objects.get(serial_number=serial_number)

        return None

    def resolve_devices(self, info, **kwargs):
        filters = utils.get_current_user_filter(info.context.user)
        return models.Device.objects.filter(**filters)

    def resolve_positions(self, info, **kwargs):
        filters = utils.get_current_user_filter(info.context.user)
        return models.Position.objects.filter(**filters)
