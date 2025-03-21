"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey_py.types import BaseModel, Nullable, UNSET_SENTINEL


class Op(str, Enum):
    r"""The operation you want to perform on the remaining count"""

    INCREMENT = "increment"
    DECREMENT = "decrement"
    SET = "set"


class UpdateRemainingRequestBodyTypedDict(TypedDict):
    key_id: str
    r"""The id of the key you want to modify"""
    op: Op
    r"""The operation you want to perform on the remaining count"""
    value: Nullable[int]
    r"""The value you want to set, add or subtract the remaining count by"""


class UpdateRemainingRequestBody(BaseModel):
    key_id: Annotated[str, pydantic.Field(alias="keyId")]
    r"""The id of the key you want to modify"""

    op: Op
    r"""The operation you want to perform on the remaining count"""

    value: Nullable[int]
    r"""The value you want to set, add or subtract the remaining count by"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["value"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class UpdateRemainingResponseBodyTypedDict(TypedDict):
    r"""The configuration for an api"""

    remaining: Nullable[int]
    r"""The number of remaining requests for this key after updating it. `null` means unlimited."""


class UpdateRemainingResponseBody(BaseModel):
    r"""The configuration for an api"""

    remaining: Nullable[int]
    r"""The number of remaining requests for this key after updating it. `null` means unlimited."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["remaining"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class UpdateRemainingResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[UpdateRemainingResponseBodyTypedDict]
    r"""The configuration for an api"""


class UpdateRemainingResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[UpdateRemainingResponseBody] = None
    r"""The configuration for an api"""
