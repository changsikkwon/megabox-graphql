import graphene
import graphql_jwt

from graphql_jwt.shortcuts import create_refresh_token, get_token
from graphql import GraphQLError
from .validators import account_validation, password_validation, phone_number_validation
from .query import UserType
from .models import User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        birth = graphene.Date(required=True)
        phone_number = graphene.String(required=True)
        account = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        if not account_validation(kwargs["account"]):
            raise GraphQLError("Incorrect Account Format")
        if not password_validation(kwargs["password"]):
            raise GraphQLError("Incorrect Password Format")
        if not phone_number_validation(kwargs["phone_number"]):
            raise GraphQLError("Incorrect Phone Number Format")
        if User.objects.filter(account=kwargs["account"]):
            raise GraphQLError("Already Exist Account")
        if User.objects.filter(email=kwargs["email"]):
            raise GraphQLError("Already Exist Email")
        if User.objects.filter(phone_number=kwargs["phone_number"]):
            raise GraphQLError("Already Exist Phone_Number")

        user = User(
            name=kwargs["name"],
            birth=kwargs["birth"],
            phone_number=kwargs["phone_number"],
            account=kwargs["account"],
            email=kwargs["email"],
        )
        user.set_password(kwargs["password"])
        user.save()

        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return CreateUser(user=user, token=token, refresh_token=refresh_token)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
