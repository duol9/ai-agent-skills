# Report Template

Use this as the default shape for a conclusion-first technical decision memo.

```markdown
# Technical Decision: [Topic]

## Recommendation
**Choose: [Option]**

[One or two sentences on the core reason.]

## Why
- [Reason 1]
- [Reason 2]
- [Reason 3]

## Criteria
| Criterion | Weight | Notes |
|-----------|--------|-------|
| Maintainability | High | Existing team will own this long term |
| Performance | Medium | Important but not dominant |

## Option Comparison
| Option | Strengths | Weaknesses | Best fit |
|--------|-----------|------------|----------|
| A | ... | ... | ... |
| B | ... | ... | ... |

## Risks And Caveats
- [Risk]
- [Risk]

## Confidence
- `High` / `Medium` / `Low`
- Explain what would most likely change the recommendation.

## Sources
- [Official docs](url)
- [Community discussion](url)

## Next Steps
1. [Prototype, benchmark, or migration step]
2. [Validation step]
3. [Rollback or checkpoint]
```

Keep the recommendation short. Put detailed nuance in later sections, not ahead of the answer.
