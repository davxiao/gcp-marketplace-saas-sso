# gcp-marketplace-saas-sso

GCP Marketplace Documentation https://cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration

Note: 
- For an end to end demo experience, you will also need a GCP marketplace SaaS listing, hosting this code somewhere as URL, and configuring the URL as the SaaS sign-up URL on the listing.
- The `x-gcp-marketplace-token` is present in the HTTP data, not in the HTTP header.
- The SSO flow described in the marketplace and the underlying token exchange mechanism is comparable to OAuth 2.0 token exchange mechanism.
- For other SSO application integrations outside of GCP Marketplace, this can be expanded by including extra claims in the JWT as long as there is an agreement between GCP and the external application.
