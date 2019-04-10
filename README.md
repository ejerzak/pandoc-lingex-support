A pandoc filter that exports latex labels and references from internal
org links.

# Use

Will convert:

- `<<ex:foo>>` to `\label{ex:foo}`
- `[[ex:foo]]` to `\ref{ex:foo}`

Intended use with the lingex package:

`\\ex. This is my example. <<ex:foo>>`

`As [[ex:foo]] shows, we're all fucked.`
