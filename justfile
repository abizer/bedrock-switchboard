set fallback

install:
  uv sync --frozen
  trunk actions enable trunk-fmt-pre-commit
  trunk actions enable trunk-fmt-pre-push

trunk-check:
  trunk check --all --fix

trunk-fmt:
  trunk fmt

test *args='-n 4':
  uv run pytest {{args}}
alias tests := test
