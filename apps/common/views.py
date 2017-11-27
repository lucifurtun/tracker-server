from django.http import HttpResponse
from graphene_django.views import GraphQLView


class CustomGraphQLView(GraphQLView):
    def dispatch(self, request, *args, **kwargs):
        if request.method.upper() == 'OPTIONS':
            """ 
            Workaround for OPTIONS request performed by angular in development mode 
            """
            return HttpResponse('ok')

        return super().dispatch(request, *args, **kwargs)
