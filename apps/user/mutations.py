import graphene
from django.contrib.auth import authenticate, login

from apps.user.nodes import UserNode


class LogIn(graphene.Mutation):
    user = graphene.Field(UserNode)

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    @classmethod
    def mutate(cls, root, info, email, password):
        user = authenticate(username=email, password=password)

        if user is None:
            raise Exception('Please enter a correct email and password')

        if not user.is_active:
            raise Exception('It seems your account has been disabled')

        login(info.context, user)
        return cls(user=user)
