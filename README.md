# gcp-marketplace-saas-sso

GCP Marketplace Documentation https://cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration

Note: 
- The `x-gcp-marketplace-token` is present in the data. (Not in the header)
- The SSO flow described in the marketplace per se is not an OAuth 2.0 flow, although the underlying token exchange mechanism is very close to OAuth 2.0 Token Exchange.
- For other SSO application outside of GCP Marketplace, this design can be expanded by including extra claims in the JWT as long as there is an agreement between GCP and the external application.
