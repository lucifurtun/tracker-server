import graphene
from graphene_django import DjangoObjectType

from apps.tracking import models, utils


class DeviceType(DjangoObjectType):
    class Meta:
        model = models.Device
        filter_fields = ['id', 'user_id', 'serial_number']
        interfaces = (graphene.relay.Node,)


class PositionType(DjangoObjectType):
    class Meta:
        model = models.Position


class Query(object):
    devices = graphene.List(DeviceType)
    positions = graphene.List(PositionType)

    def resolve_devices(self, info, **kwargs):
        filters = utils.get_current_user_filter(info.context.user)
        return models.Device.objects.filter(**filters)

    def resolve_positions(self, info, **kwargs):
        filters = utils.get_current_user_filter(info.context.user)
        return models.Position.objects.filter(**filters)
