# Build a blyg

Three ways in, ordered by how much work they are. The first one is free and you
may have done it already.

## 1. You might already be halfway in

If your site has an **RSS or Atom feed**, blygs can subscribe to you today. No
software to install, no change to your site, no cooperation required at your
end — a blyg reader resolves your feed and imports your items the same way it
imports another blyg's.

What you don't get, without going further, is being *quotable*: transclusion —
someone baking a snapshot of your writing into their piece, with provenance
recording exactly which version they quoted — needs your side to publish the
item documents that make a snapshot possible.

So: readable is free. Quotable is the upgrade.

**Try it:** [submit your feed to the directory](https://blygger.com) and see
what a blyg client makes of it. Submission runs the real resolution algorithm
and tells you what it found.

## 2. Host a blyg on Cloudflare

The reference client is a small Cloudflare Worker — publishing, subscribing,
blogrolls, curated lists, and instructed generation, with the published output
as pure static files.

**Status: planned, not shipped.** A template repository plus an interactive
`npm run init` that provisions the database and storage, writes your config,
applies migrations, and prompts for your secrets. Design is written up in
[`self-host-plan.md`](https://github.com/blygger/blygger-spec/blob/main/docs/self-host-plan.md);
the tooling is not built yet.

Standing one up by hand is possible today — the client is
[MIT-licensed](https://github.com/blygger/blygger-spec) and the two live nodes
were both built that way — but it is about a dozen steps with two
copy-the-generated-id-back-into-config loops, which is exactly what the tooling
exists to remove. If you want to do it anyway, the deployment shape is in
`worker/wrangler.jsonc`.

## 3. Build a client

The most useful thing anyone could do right now.

- **[The spec](/spec/0.2/)** — standalone and complete. A `/spec/{version}/` URL
  hands you one whole document; you never chase deltas through a changelog.
- **[Technical notes](/notes/)** — non-normative records of *why*, especially of
  designs that were rejected.
- **[The CSS contract](https://github.com/blygger/blygger-spec/blob/main/docs/css-contract.md)**
  — which classes are visible on the wire and what any client owes them.
- **Conformance levels L0–L3** are strict supersets, and unknown constructs are
  ignored rather than rejected, so a partial implementation is a *conformant*
  implementation.

**The open gap, and the 1.0 gate:** there is exactly one reference
implementation. One implementation is not a protocol — it is a program with a
spec next to it. What's wanted is a second one on a deliberately different
substrate: local-first, a folder on a laptop, authoring on-device, deploying to
a dumb static host. It is undesigned and unstarted.

## What you're signing up for

**No version before 1.0 is stable, including the wire format.** Building the
reference client is how this protocol gets tested, so the spec changes when
building finds something — twice in the last month it did.

That is a real cost and it is stated here rather than buried: read it,
implement it, argue with it, but don't build something load-bearing on it yet
and expect the ground to hold still.

What *is* stable, because it costs nothing to promise: every blyg feed is valid
RSS, the published surface is static files, and nothing about the protocol
requires a company in the middle.
