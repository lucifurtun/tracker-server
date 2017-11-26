import graphene

from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from graphql_jwt.utils import jwt_encode, jwt_payload


class UserNode(DjangoObjectType):
    token = graphene.String()

    class Meta:
        model = get_user_model()

    def resolve_token(self, info, **kwargs):
        if info.context.user != self:
            return None

        payload = jwt_payload(self)
        return jwt_encode(payload)
