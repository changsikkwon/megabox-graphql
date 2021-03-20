import graphene

from django.contrib.auth.hashers import make_password
from graphql import GraphQLError
from .validators import account_validation, password_validation, phone_number_validation
from .query import UserType
from .models import User


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        birth = graphene.Date(required=True)
        phone_number = graphene.String(required=True)
        account = graphene.String(required=False)
        password = graphene.String(required=True)
        email = graphene.String(required=False)
        is_user = graphene.Boolean(required=True)

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, **kwargs):
        if kwargs["is_user"]:
            if not kwargs.get("account", None) and not kwargs.get("email", None):
                raise GraphQLError("Does Not Exist Key Account Or Email")
            if not account_validation(kwargs["account"]):
                raise GraphQLError("Incorrect Account Format")
            if User.objects.filter(account=kwargs["account"]):
                raise GraphQLError("Already Exist Account")
            if User.objects.filter(email=kwargs["email"]):
                raise GraphQLError("Already Exist Email")

        if not password_validation(kwargs["password"]):
            raise GraphQLError("Incorrect Password Format")
        if not phone_number_validation(kwargs["phone_number"]):
            raise GraphQLError("Incorrect Phone Number Format")
        if User.objects.filter(phone_number=kwargs["phone_number"]):
            raise GraphQLError("Already Exist Phone_Number")

        user = User(
            name=kwargs["name"],
            birth=kwargs["birth"],
            phone_number=kwargs["phone_number"],
            account=kwargs.get("account", None),
            password=make_password(kwargs["password"]),
            email=kwargs.get("email", None),
            is_user=kwargs["is_user"],
        )

        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
