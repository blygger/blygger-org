# Two studio releases, and planning for private posts and enterprise use

*Blygger Studio 0.52.0 and 0.53.0 shipped on 2026-11-04, and both are live on the
four reference nodes. The day also started two planning threads: private posts, and
Blygger inside organisations. This post summarises both. The full record is the
[program devlog](https://github.com/blygger/blygger-spec/blob/main/DEVLOG.md).*

## Faster reading, and reads that cost less

**0.52.0** is mostly about the reader using less of the database.

- **Batched reads** (Kyle Mathews, studio#114). Independent reads on a studio page now
  travel together in one request. On the server, the database statements in each
  batch share calls. Mentions opens with 10 posts and 10 mentions each. In review,
  the browser half turned out to wait on a timer, which browsers throttle in background
  tabs; Kyle switched it to dispatch without timers before it merged.
- **Two table scans removed** (studio#113, reported by patwater, fixed in #115). On
  Cloudflare's free plan, database rows read count against a daily limit, and one
  owner's reader was using it up. The main cause, the inbox ordering, was fixed in
  0.49.12, so nodes older than that should upgrade. The report also surfaced two
  lookups that still read whole tables: finding an item you follow by its id, and
  listing which collections each reading entry is in. Both now use an index.
- **Collections without your own collection feeds** (Aneesh Sathe, studio#112). You
  can subscribe to another blyg's public collection whether or not your node publishes
  collection feeds of its own.

## Search, and studios you can tell apart

**0.53.0** adds things you can see.

- **Search on the reading and compose pages** (studio#120). It is the same search the
  `[[` picker runs. Type in the box at the top, and the results replace the list. The
  search goes in the address, so the back button returns to your results. On the
  reading page, it searches the source you have selected, with a button to widen it.
  On the compose page, it searches your own blyg by default, drafts included.
- **The login page wears your blyg's theme** (studio#119). It used to be the studio's
  default blue.
- **Each studio's browser tab says which blyg it is** (studio#121). The title names the
  blyg, and the ❝ icon takes the theme's accent colour. If you run several blygs, you
  can now tell the tabs apart without clicking in.
- **Read batches are more robust** (Kyle Mathews, studio#116). A malformed address in
  one read no longer fails the reads around it.

Both releases have announcements on this blyg with their full notes. The release posts
for 0.49.1, 0.49.12, 0.50.0 and 0.51.0, which had been missed, went up the same day.

## Planning: private posts

A **private** level for posts is being worked out. It is for finished work you
haven't decided whether to publish. The current shape, from an exploration in
blygger-spec (`plans/private-items-proposal.md`):

- **Visibility goes user / group / public**, like Unix permissions, and is separate
  from draft. A private post can have versions and pending changes like a public one.
  Only public posts are ever served.
- **A private post can be quoted and linked from your own drafts and private posts.**
  Publishing anything that refers to it is blocked until you remove the reference or
  make the private post public first.
- **Group** (a named set of readers) is the protocol's deferred privileged-access level.
  It waits for a design round of its own.
- One question goes to the protocol's design review: when a post that reached its third
  private version goes public, does it start at version 1 on the wire?

Nothing is built yet.

## Planning: Blygger inside organisations

A draft RFC asks whether anything fundamental stops Blygger being used inside an
organisation: on an internal network, behind single sign-on, under retention rules.
The short answer is **no, not at the protocol level.**

- Nothing in the protocol assumes the public internet. A blyg on an internal network,
  or behind a sign-on gate, is a blyg whose audience is everyone who can reach it.
- Different readers seeing different posts *within one blyg* is the deferred
  privileged-access level again. One blyg per audience works today.
- The real risks are a quote of internal work copying it out (a quote bakes the text)
  and retention law running against "published stays published".

The RFC is written for anyone building an enterprise product on Blygger, which is
expected to be a client of its own. After a design review it will be published here
for comment, then become a technical note.

## Where the code is

- [Blygger Studio releases](https://github.com/blygger/blygger-studio/releases)
- [The 0.4 spec](https://blygger.org/spec/0.4/), now at its ninth revision
- [Modding the Studio](https://github.com/blygger/blygger-studio/blob/main/docs/mods.md),
  published this week, linked from the [ecosystem page](https://blygger.org/ecosystem/)
