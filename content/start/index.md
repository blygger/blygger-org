# Build a blyg

Three ways in, ordered by how much work they are. The first one is free and you
may have done it already.

## 1. You might already be halfway in

If your site has an **RSS or Atom feed**, blygs can subscribe to you today, with
nothing to install and no change to your site. What you don't get is being
*quotable*: quoting by reference needs your side to publish the item documents
a snapshot is made from. Readable is free; quotable is the upgrade.

**Try it:** [submit your feed to blygger.com](https://blygger.com). Submission
runs the real resolution algorithm and tells you what it found.

## 2. Host a blyg on Cloudflare

**[Blygger Studio](https://github.com/blygger/blygger-studio)** is the reference
client: a Cloudflare Worker that publishes, subscribes, keeps collections and
generates text with your own model, while the published output stays static
files. You need a Cloudflare account and a domain on it. There are two install
paths, a prebuilt Worker download or the source; the
[README](https://github.com/blygger/blygger-studio#installation) has both. From
source:

```
git clone --branch vVERSION https://github.com/blygger/blygger-studio.git
cd blygger-studio
git switch -c my-blyg
npm ci
npx wrangler login
npm run init
npm run deploy
```

`init` asks which Cloudflare account and domain to use, creates the database
and media bucket, applies migrations and sets your secrets. It can resume after
a failed step. Your blyg is then at `https://blyg.yourdomain.com/`, with the
studio at `/studio`.

- **Stay current.** Before 1.0 the wire format can change between releases, so
  upgrading is how you stay legible to the blygs reading you. Each changelog
  entry has a `Migrations:` line; read it before you upgrade.
- **Use a subdomain.** A path mount (`yourdomain.com/blyg/`) works, but the
  studio's `/studio` and `/api` sit at the host root and can collide with a site
  already there.
- **Leaving is a command.** `npm run export` writes your public blyg as static
  files. For a full backup, drafts, settings and subscriptions included, use
  More → download backup in the studio, or `npm run backup` for a large blyg.
- **List it, if you like,** at [blygger.com](https://blygger.com), which is how
  readers who don't know you yet find you. Nothing in the protocol needs a
  registry.

Something wrong with the client? [File it against Blygger
Studio](https://github.com/blygger/blygger-studio/issues/new/choose), not
against the spec, unless another client would have to change too.

## 3. Build a client

**Most of the protocol's life is here.** Independent clients publish a large
share of the live blygs: standalone clients, integrations that teach Obsidian,
Hugo, WordPress and Logseq gardens to emit a blyg, and tools that write into an
existing one. The [ecosystem index](/ecosystem/) lists every known one. If you
build one, [add it to the
index](https://github.com/blygger/blygger-org/issues/new/choose): clients are
written from the spec, so a new one is invisible until its author says so.

### Which text to build against

- **The living spec, [blygger.org/spec/](/spec/)**: the highest-numbered
  version, standalone and complete. Build against this.
- **A dated snapshot, `/spec/{version}/{date}/`**: immutable. Pin one when you
  need the text to hold still, and say which one you built against. Each
  snapshot links a diff to the one before.
- **Not the spec:** the living document's last section, which holds constructs
  decided but not yet built, and can still move; the plan documents; and the
  reference client's source. When the client and the spec disagree, the client
  has a bug.

Older versions stay conformant: levels are strict supersets and unknown
constructs are ignored, so an older client lacks the newer constructs and
nothing more.

Building a decided-but-unbuilt construct early is the most useful thing an
implementer can do, because that is how a wrong shape is found while it is
cheap to change. Say which snapshot you built against, and [file what you
find](https://github.com/blygger/blygger-spec/issues).

### Do not ship a generic default title

Blygger Studio once shipped `"blyg"` as every blyg's default title. Within
weeks two unrelated blygs were publishing under that name, and blygger.com
briefly held a newcomer's blyg as a suspected impersonation. A default every
installation shares is a name nobody chose. Instead, derive the title from the
deployment's own host (`blyg.example.com` becomes `example.com`, as Studio now
does), ask at install time, or publish no title at all. The general rule: **a
default identical across installations destroys information.**

### Also worth reading

- **[Technical notes](/notes/)**: why things were decided, including the
  rejected designs.
- **[RFCs](/rfcs/)**: proposals open for comment.
- **[The CSS contract](https://github.com/blygger/blygger-spec/blob/main/docs/css-contract.md)**:
  which classes are visible on the wire and what any client owes them.
- **[The conformance toolkit](https://github.com/blygger/blygger-spec/tree/main/conformance)**:
  the clause register, JSON Schemas, a reader suite and a live crawler.

**Still wanted:** a client on a deliberately different substrate, **local-first**:
a folder on a laptop, authoring on-device, deploying to a plain static host,
with no server in the publishing path. That is the real test of the
static-files-and-RSS claim, because nothing dynamic exists to paper over a gap
in the spec.

## What you're signing up for

**No version before 1.0 is stable, including the wire format.** Building
clients is how this protocol gets tested, so the spec changes when building
finds something. Read it, implement it, argue with it, but don't build
something load-bearing on it yet.

What *is* stable: every blyg feed is valid RSS, the published surface is static
files, and nothing in the protocol requires a company in the middle.
