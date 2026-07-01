# Security

Use `/接口安全` and `/配置安全` for backend and project safety checks.

## Security Principle

Do not ask "is it safe?" Ask:

- What is the risk?
- Where is the rule?
- Which file or framework mechanism handles it?
- How was it verified?
- What remains unverified?

Security must include negative cases, not only normal flows.

For non-technical users, every security result must be explainable in plain Chinese. If the user cannot understand what risk was blocked, the security explanation is not complete.

## `/接口安全`

Check these boundaries:

- Authentication: who sent the request and whether they are logged in.
- Authorization: whether that user can do this action.
- Input validation: whether frontend data is trusted too much.
- Data ownership: whether users can access or change other people's data.
- Password and administrator account rules.
- Injection risk.
- Public/private exposure: whether pages, files, uploads, generated assets, previews, or admin routes are accessible to people who should not see them.
- Over-defense and dead code.

Output a security boundary table:

- Interface.
- Risk.
- Rule.
- Processing location.
- Validation method.
- Evidence.
- Status.

Do not summarize security as "handled" or "safe". Each row must name the risk, rule, processing location, and proof.

## Frontend Input Is Not Trusted

Backend must re-check data that affects:

- Identity.
- Role.
- Permission.
- Money.
- Inventory.
- Data ownership.
- Database writes.
- Status changes.

Frontend validation improves experience but does not secure backend rules.

## AI And LLM Feature Safety

Use this section when the project includes AI chat, AI generation, document analysis, agent actions, RAG/search, tool calls, plugins, workflow automation, or any model that reads user/private/project data.

Check:

- Prompt injection: external text, uploaded files, retrieved docs, web pages, user content, or provider responses must not be allowed to override system/business rules.
- Sensitive information disclosure: prompts, logs, traces, model outputs, screenshots, exports, and error messages must not reveal secrets, private docs, customer data, tokens, or internal instructions.
- Untrusted output handling: model output must not be executed, rendered as raw HTML, used as SQL, used as shell commands, or trusted as a permission/payment/business decision without validation.
- Excessive agency: AI tools must not delete data, send emails, charge money, publish content, change permissions, rotate secrets, or call external APIs without scoped permission and human confirmation when impact is high.
- Cost and abuse: model calls need rate limits, quotas, timeout, retry rules, and user-visible failure states when relevant.
- Data retention: know what is sent to the provider, what is stored locally, what can be deleted, and what consent or notice is needed.

Output an AI safety table:

- AI feature.
- Data entering the model.
- Model/provider.
- Action allowed.
- Action forbidden.
- Validation location.
- Human confirmation needed.
- Evidence.
- Status.

Do not present an AI feature as production-ready if prompt injection, sensitive output, tool permissions, and provider data handling are unreviewed.

## Password And Admin Accounts

Check:

- Password length.
- Character rules.
- Common weak password rejection when appropriate.
- Password hash storage.
- Login failure limits when needed.
- Stronger administrator requirements.
- Reset and change-password flows.

Never store plaintext passwords.

## Permissions

Separate:

- Authentication: who you are.
- Authorization: what you can do.

Check vertical privilege issues, such as normal users calling admin APIs.

Check horizontal privilege issues, such as a logged-in user changing an ID and seeing another user's data.

Create a permission table:

- Interface.
- Login required.
- Roles allowed.
- Own-data only.
- Admin access.
- Check location.
- No-permission response.
- Test evidence.

## Injection

User input must not be directly inserted into:

- SQL.
- Database queries.
- System commands.
- HTML.
- Templates.

Prefer mature mechanisms:

- ORM.
- Parameterized queries.
- Query builders.
- Whitelist fields.
- Escaping or sanitization where appropriate.

Be suspicious of custom filtering code presented as complete security.

## Over-Defense

Security is not maximum code volume.

Reject:

- Repeated checks already guaranteed by the framework.
- Impossible branches.
- Dead code.
- New security wrappers without a real risk.

Keep strict checks where business impact exists: login, permission, ownership, money, inventory, status, sensitive data.

## `/配置安全`

Check:

- Secrets hard-coded in source.
- Database URL/password.
- Login token secrets such as JWT keys.
- Third-party API keys.
- Initial administrator password.
- Payment or notification secrets.
- Whether real secrets appeared in repo history.
- Whether example config files contain placeholders only.
- Whether key rotation is needed.

## Logs

Logs must not record raw:

- Passwords.
- Tokens.
- Secret keys.
- Phone numbers when not needed.
- ID numbers.
- Payment data.
- Sensitive callbacks.

Ask for normal request log and error log examples.

## Dependencies

List frameworks, libraries, and SDKs with versions. Pay special attention to:

- Network requests.
- Authentication.
- Encryption.
- File upload.
- Database connection.
- Logging.

Check current advisories when risk matters. Upgrade only after explaining impact.

## Public Exposure

Before any public URL, preview deployment, client handoff, or shared demo:

- Confirm whether the app, preview, storage bucket, uploaded files, generated files, admin pages, API docs, logs, and internal docs are public or private.
- Check platform privacy settings instead of assuming defaults are safe.
- Make sure search engines should or should not index the app.
- Verify no real customer data, medical/financial/private information, internal planning, or secret-like content is visible.
- Verify admin routes and internal tools require authentication and authorization.

For non-technical users, explain the difference between "anyone with the link can open it" and "only approved users can access it".

## Third-Party Provider Security

For third-party APIs, SDKs, OAuth, payment, webhooks, maps, AI providers, storage, messaging, analytics, or platform services, require official documentation evidence before implementation.

Check:

- Secret storage and rotation.
- OAuth scopes or API permissions.
- Webhook signature verification.
- Replay protection.
- Idempotency for payment, order, message, or state-changing calls.
- Rate limits and retry strategy.
- Sensitive data sent to provider.
- Sensitive data logged locally.
- Callback URL/domain verification.
- Sandbox versus production separation.
- User-facing failure state.

If docs are unavailable, mark the integration security review `未验证`.

## Payment And Entitlement Security

For payments, subscriptions, memberships, paid credits, usage quotas, paid downloads, or paid reports:

- Backend must own paid access checks.
- Provider webhook or server verification must be the source of payment truth.
- Webhook signatures must be verified.
- Duplicate webhook events must be idempotent.
- Refund, cancel, expiry, dispute, and failed renewal must update or remove entitlement according to product rules.
- Frontend success pages, local storage, URL parameters, or disabled buttons are not entitlement truth.
- Admin manual grants/revokes require strong authorization and audit logs.

Do not mark paid features ready if entitlement truth and provider verification are `未验证`.

## Database Operation Safety

For important data, list:

- Which interfaces read it.
- Which interfaces modify it.
- Which interfaces delete it.
- Login checks.
- Permission checks.
- Ownership checks.
- Business rules.
- Soft delete needs.
- Transaction needs.
- Audit log needs.

Operations touching multiple tables, money, inventory, coupon, balance, or payment records usually need transactions.

Prefer validating normal business behavior through the API path, because real users do not directly edit the database. Use database checks as before/after evidence, not as a substitute for endpoint validation.

## Evidence

Security validation should include:

- Normal request.
- Invalid parameters.
- Not logged in.
- No permission.
- Accessing another user's data.
- Database before/after evidence.
- Relevant logs.

Mark missing proof as `未验证`.

For each new or changed interface, do a business-and-security double validation:

- Normal request succeeds.
- Invalid input is rejected.
- Not-logged-in access is blocked when required.
- Wrong-role access is blocked.
- Cross-user or cross-tenant data access is blocked when ownership matters.
- Database before/after evidence matches the business rule.
- Logs help diagnose the action without leaking sensitive data.
