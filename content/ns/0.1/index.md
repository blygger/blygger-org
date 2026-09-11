# The `blyg:` XML Namespace

**`https://blygger.org/ns/0.1`**

You have most likely arrived here because you found this URI in the
`xmlns:blyg` attribute of a Blygger feed and followed it to see what it is.
This page is that answer.

This URI is a **namespace name** — an identifier, not a location. It exists to
make the `blyg:` element names in a Blygger feed unambiguous, so that they
cannot collide with identically-named elements from any other vocabulary in
the same document. Nothing is required to fetch it, and nothing in the
protocol changes based on what it returns. XML namespace names are not
required to resolve at all; this one does, as a courtesy to whoever is
reading a feed and wondering.

There is no schema here. No DTD, no XSD, no RDDL document is served at this
URI, and the protocol never refers to one. The normative definition of every
construct below is prose, in the specification linked at the foot of this
page.

This page is **descriptive, not normative**. Where it and the specification
disagree, the specification is correct.

## Elements in this namespace

A Blygger feed is ordinary RSS 2.0. Everything specific to Blygger lives in
this namespace, so a reader that knows nothing about Blygger sees a valid
feed and ignores the rest.

Two elements appear once per feed, inside `<channel>`:

| Element | Content |
|---|---|
| `blyg:level` | Conformance level of this blyg, as an integer |
| `blyg:manifest` | Absolute URL of the blyg's `blyg.json` manifest |

`blyg:manifest` is the load-bearing one for implementors: it is what makes a
plain RSS feed upgradeable to a full Blygger subscription, and what lets an
ordinary OPML blogroll carrying only feed URLs resolve to blygs without any
custom OPML extension.

Five appear once per `<item>`:

| Element | Content |
|---|---|
| `blyg:id` | The item's stable identifier — constant across every version |
| `blyg:kind` | The item's kind (`fragment`, `thread`, `withdrawn`) |
| `blyg:version` | Version number of the publish event this entry announces |
| `blyg:created` | ISO 8601 timestamp of the item's first publication |
| `blyg:item` | Absolute URL of the item's JSON document |

The division of labour between these and the feed's own elements is the
protocol's central structural idea. The feed is a **notification plane**: a
lossy, bounded, reverse-chronological signal that something changed. The item
documents that `blyg:item` points at are the **state plane**: ground truth,
complete, and the only surface a reader should trust for content. A feed
entry tells you to go look; the item document is what you are looking at.

Readers must ignore `blyg:*` elements they do not recognise, rather than
rejecting the feed or the entry containing them. That rule is what allows
later protocol versions to add elements here without breaking readers built
against earlier ones.

## The `blyg:` GUID scheme

One more construct carries the `blyg:` name without being an element in this
namespace. Each entry's `<guid isPermaLink="false">` is a string of the form:

```
blyg:{id}:v{n}
```

This is a plain RSS guid, and its `blyg:` is a URI-scheme-like prefix in
ordinary character data — namespace declarations have no bearing on it.

It is deliberately per-version. An ordinary RSS reader dedupes by guid, so
republishing an edited item under a new version produces a genuinely new
entry and the edit resurfaces — which is the behaviour a changelog-shaped
medium wants from readers that know nothing about it. A Blygger-aware reader
ignores that and rolls entries up by `blyg:id` instead, showing one live item
at its highest version.

## Versioning of this namespace

This URI is permanent. It does not track the protocol version, and never
will: the `0.1` inside it is part of the token's spelling, fixed at the
moment the namespace was minted, not a claim about which protocol version
produced the feed you found it in. A feed whose manifest declares protocol
`0.2` — or, one day, `1.0` — declares this same namespace, the way Dublin
Core elements still live at `/1.1/` and Atom's namespace still says `2005`.

This is deliberate. Readers must ignore `blyg:` elements they do not
recognise, which is what lets later protocol versions add vocabulary to
this namespace without breaking earlier readers — and a namespace URI that
changed with each version would break exactly the readers that rule exists
to protect, while forcing every reader to enumerate all the URIs ever
minted. The protocol's version signal is the manifest's `blyg` key, not
this URI. If a future vocabulary ever needed incompatible semantics — none
is expected — it would arrive under a new URI, leaving this one meaning
what it means now, forever.

## The specification

The protocol is specified in prose, versioned separately from this namespace
name, at:

- **[blygger.org/spec/](/spec/)** — all versions and dated snapshots
- **[blygger.org/spec/0.1/](/spec/0.1/)** — current working draft

Feed construction is specified in §7 of the spec; the manifest in §4; item
documents in §5; reader conformance, including the ignore-unknowns rule
above, in §11.

Every specification version below 1.0 is a working draft, and the wire
surface carries no stability promise until 1.0. Source, including the
reference implementation that produces the feeds this namespace appears in,
is at [blygger/blygger-spec](https://github.com/blygger/blygger-spec).
