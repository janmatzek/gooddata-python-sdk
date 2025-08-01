# (C) 2024 GoodData Corporation
from __future__ import annotations

from typing import Any, Optional

import attr
from gooddata_api_client.model.json_api_identity_provider_in import JsonApiIdentityProviderIn
from gooddata_api_client.model.json_api_identity_provider_in_attributes import JsonApiIdentityProviderInAttributes
from gooddata_api_client.model.json_api_identity_provider_in_document import JsonApiIdentityProviderInDocument
from gooddata_api_client.model.json_api_identity_provider_patch import JsonApiIdentityProviderPatch
from gooddata_api_client.model.json_api_identity_provider_patch_document import JsonApiIdentityProviderPatchDocument

from gooddata_sdk.catalog.base import Base
from gooddata_sdk.utils import safeget


@attr.s(auto_attribs=True, kw_only=True)
class CatalogIdentityProviderDocument(Base):
    data: CatalogIdentityProvider

    @staticmethod
    def client_class() -> type[JsonApiIdentityProviderInDocument]:
        return JsonApiIdentityProviderInDocument


@attr.s(auto_attribs=True, kw_only=True)
class CatalogIdentityProvider(Base):
    id: str
    attributes: Optional[CatalogIdentityProviderAttributes] = None

    @staticmethod
    def client_class() -> type[JsonApiIdentityProviderIn]:
        return JsonApiIdentityProviderIn

    @classmethod
    def init(
        cls,
        identity_provider_id: str,
        custom_claim_mapping: Optional[dict[str, str]] = None,
        identifiers: Optional[list[str]] = None,
        oauth_client_id: Optional[str] = None,
        oauth_client_secret: Optional[str] = None,
        oauth_issuer_location: Optional[str] = None,
        saml_metadata: Optional[str] = None,
        idp_type: Optional[str] = None,
        oauth_issuer_id: Optional[str] = None,
        oauth_subject_id_claim: Optional[str] = None,
        oauth_custom_auth_attributes: Optional[dict[str, str]] = None,
        oauth_custom_scopes: Optional[list[str]] = None,
    ) -> CatalogIdentityProvider:
        return cls(
            id=identity_provider_id,
            attributes=CatalogIdentityProviderAttributes(
                custom_claim_mapping=custom_claim_mapping,
                identifiers=identifiers,
                oauth_client_id=oauth_client_id,
                oauth_client_secret=oauth_client_secret,
                oauth_issuer_location=oauth_issuer_location,
                saml_metadata=saml_metadata,
                idp_type=idp_type,
                oauth_issuer_id=oauth_issuer_id,
                oauth_subject_id_claim=oauth_subject_id_claim,
                oauth_custom_auth_attributes=oauth_custom_auth_attributes,
                oauth_custom_scopes=oauth_custom_scopes,
            ),
        )

    @classmethod
    def from_api(cls, entity: dict[str, Any]) -> CatalogIdentityProvider:
        ea = entity["attributes"]
        attr = CatalogIdentityProviderAttributes(
            custom_claim_mapping=safeget(ea, ["custom_claim_mapping"]),
            identifiers=safeget(ea, ["identifiers"]),
            oauth_client_id=safeget(ea, ["oauth_client_id"]),
            oauth_client_secret=safeget(ea, ["oauth_client_secret"]),
            oauth_issuer_location=safeget(ea, ["oauth_issuer_location"]),
            saml_metadata=safeget(ea, ["saml_metadata"]),
            idp_type=safeget(ea, ["idp_type"]),
            oauth_issuer_id=safeget(ea, ["oauth_issuer_id"]),
            oauth_subject_id_claim=safeget(ea, ["oauth_subject_id_claim"]),
            oauth_custom_auth_attributes=safeget(ea, ["oauth_custom_auth_attributes"]),
            oauth_custom_scopes=safeget(ea, ["oauth_custom_scopes"]),
        )
        return cls(
            id=entity["id"],
            attributes=attr,
        )

    @classmethod
    def to_api_patch(cls, identity_provider_id: str, attributes: dict) -> JsonApiIdentityProviderPatchDocument:
        return JsonApiIdentityProviderPatchDocument(
            data=JsonApiIdentityProviderPatch(
                id=identity_provider_id, attributes=JsonApiIdentityProviderInAttributes(**attributes)
            )
        )


@attr.s(auto_attribs=True, kw_only=True)
class CatalogIdentityProviderAttributes(Base):
    custom_claim_mapping: Optional[dict[str, str]] = None
    identifiers: Optional[list[str]] = None
    oauth_client_id: Optional[str] = None
    oauth_client_secret: Optional[str] = None
    oauth_issuer_location: Optional[str] = None
    saml_metadata: Optional[str] = None
    idp_type: Optional[str] = None
    oauth_issuer_id: Optional[str] = None
    oauth_subject_id_claim: Optional[str] = None
    oauth_custom_auth_attributes: Optional[dict[str, str]] = None
    oauth_custom_scopes: Optional[list[str]] = None

    @staticmethod
    def client_class() -> type[JsonApiIdentityProviderInAttributes]:
        return JsonApiIdentityProviderInAttributes
