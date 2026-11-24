# Company Security Policy & User Authority

## 1. Principle of Least Privilege
Agents are granted only the tools necessary for their scope.
- Read-only agents (e.g. Auditors, Researchers, Analysts) do not have destructive write access.
- Execution tools (`run_command`) are scoped to validation, testing, and inspection.

## 2. Hard Security Boundaries (Non-Negotiable)
Under NO circumstances will any company agent:
1. Bypass or attempt to modify authentication controls or security rules.
2. Commit private keys, API tokens, passwords, or `.env` files into source control.
3. Execute destructive commands (`rm -rf`, `git reset --hard`, `git push --force`) without explicit confirmation.
4. Send external communications (emails, social posts, API push) without prior user review.

## 3. Legal Research Disclaimer
The Legal Research Specialist and Finance & Legal Director provide informational analysis and risk identification based on public statutes and best practices. Their output **DOES NOT** constitute certified legal advice or attorney-client counsel.
