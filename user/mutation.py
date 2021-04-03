import graphene

from graphql_jwt.shortcuts import create_refresh_token, get_token
from graphql import GraphQLError
from datetime import datetime
from .validators import account_validation, password_validation, phone_number_validation
from .query import UserType
from .models import User
from .utils import login_required
from django_globals import globals


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

        user = User(**kwargs)
        user.set_password(kwargs["password"])
        user.save()

        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return CreateUser(user=user, token=token, refresh_token=refresh_token)


class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        name = graphene.String(required=False)
        birth = graphene.Date(required=False)
        phone_number = graphene.String(required=False)
        account = graphene.String(required=False)
        password = graphene.String(required=False)
        email = graphene.String(required=False)

    @login_required
    def mutate(self, info, **kwargs):
        if "account" in kwargs:
            if not account_validation(kwargs["account"]):
                raise GraphQLError("Incorrect Account Format")
            if User.objects.filter(account=kwargs["account"]):
                raise GraphQLError("Already Exist Account")
        if "phone_number" in kwargs:
            if not phone_number_validation(kwargs["phone_number"]):
                raise GraphQLError("Incorrect Phone Number Format")
            if User.objects.filter(phone_number=kwargs["phone_number"]):
                raise GraphQLError("Already Exist Phone_Number")
        if "email" in kwargs:
            if User.objects.filter(email=kwargs["email"]):
                raise GraphQLError("Already Exist Email")

        user = User.objects.get(id=globals.user)
        kwargs["updated_at"] = datetime.now()

        for key, value in kwargs.items():
            setattr(user, key, value)

        if "password" in kwargs:
            if not password_validation(kwargs["password"]):
                raise GraphQLError("Incorrect Password Format")
            user.set_password(kwargs["password"])

        user.save()

        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return UpdateUser(user=user, token=token, refresh_token=refresh_token)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
