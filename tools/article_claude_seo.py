"""Article: how to automate SEO work with Claude. Loaded by tools/articles.py."""

ARTICLE = dict(
    slug="how-to-automate-seo-with-claude",
    title="How to Automate SEO with Claude: 13 Prompts, a Workflow and a Checklist",
    date="2026-10-10T11:00:00",
    excerpt="A practical guide to automating SEO work with Claude. Learn what data to gather, get 13 copy-ready prompts for audits, content, local visibility and reporting, and use a checklist you can run every month.",
    takeaways=[
        "Claude is strong at analysis and drafting when you give it exported data and clear rules. It cannot see your live rankings unless you provide them.",
        "Build one reusable business context, then run a repeatable monthly loop: export, analyze, decide, ship and measure.",
        "Automate the analysis, keep a person in charge of changes that go live, and check every number against its source.",
    ],
    flow=["Load your context", "Export your data", "Analyze and prioritize", "Ship and measure"],
    body="""
<p>Most SEO work is repetitive. You export data, scan for patterns, decide what to fix, write new copy and check the results. Claude can do much of the scanning and drafting, which frees you to make the decisions.</p>
<p>This guide shows how to set that up. It covers what to prepare, 13 prompts you can copy, a full monthly workflow, a checklist and the guardrails that keep automated SEO safe.</p>

<h2>What does automating SEO with Claude really mean?</h2>
<p>It does not mean letting an AI change your website unsupervised. It means turning slow, manual analysis into a fast, repeatable routine where you stay in control of decisions.</p>
<table>
  <thead><tr><th>Task</th><th>Claude is good at</th><th>You still need to</th></tr></thead>
  <tbody>
    <tr><td>Finding patterns in exported data</td><td>Scanning thousands of rows quickly</td><td>Confirm the export is complete and the date range is right</td></tr>
    <tr><td>Writing titles and descriptions</td><td>Producing several options fast</td><td>Choose the one that matches the page and the promise</td></tr>
    <tr><td>Reviewing crawl files</td><td>Grouping issues by severity</td><td>Check that each issue is real before fixing it</td></tr>
    <tr><td>Drafting content briefs</td><td>Outlines and question lists</td><td>Add real expertise, examples and sources</td></tr>
    <tr><td>Summarizing performance</td><td>Plain-language reports</td><td>Decide which changes matter most</td></tr>
  </tbody>
</table>

<h2>What do you need before you start?</h2>
<p>Gather these inputs once. Most monthly runs only need a refresh of the exports.</p>
<table>
  <thead><tr><th>Input</th><th>Why it matters</th><th>Where to get it</th></tr></thead>
  <tbody>
    <tr><td>Search Console performance export</td><td>Real queries, pages, clicks and positions</td><td>Search Console, Performance report, export to CSV</td></tr>
    <tr><td>Analytics data</td><td>Conversions and behavior on key pages</td><td>Google Analytics 4 reports</td></tr>
    <tr><td>Crawl export</td><td>Technical issues across the whole site</td><td>A site crawler such as Screaming Frog, exported to CSV</td></tr>
    <tr><td>List of money pages</td><td>The pages that drive inquiries or sales</td><td>Your own list, ranked by revenue or leads</td></tr>
    <tr><td>Keyword data</td><td>Opportunities your site is missing</td><td>Your keyword tool, exported with volume and difficulty</td></tr>
    <tr><td>Business profile data</td><td>Local categories, services, reviews and posts</td><td>Business Profile dashboard and a manual copy of key fields</td></tr>
  </tbody>
</table>
<div class="note"><strong>Important:</strong> Claude works with what you give it. It can read files you upload and pages you point it to, but it cannot see your accounts unless you provide an export or use a connected tool you have authorized.</div>

<h2>Step 1: Load your business context</h2>
<p>Paste this once at the start of a project. Every later prompt becomes sharper because Claude knows who you are and what matters.</p>
<h3>Prompt 1: Business context</h3>
<pre><code>You are my SEO analyst. Save the context below and use it for every task in this project. Do not ask me for it again.

Business: [business name], website [URL], Google Business Profile [URL]
Primary service: [service]
Other services: [service 2], [service 3]
Service areas: [city 1], [city 2], [city 3]
Ideal customer: [one sentence]
90-day goal: [for example, more qualified inquiries from search]
Biggest SEO problem right now: [one honest sentence]

Rules:
- Lead with quick wins, then longer projects.
- Label each recommendation high, medium or low impact, with an estimate of how long results take.
- Use tables for comparisons.
- If you are unsure, say so. Do not guess numbers.
- Never invent reviews, statistics, awards or client names.</code></pre>

<h2>Step 2: Analyze search performance</h2>
<p>This is the core of the monthly loop. Export the last 90 days of queries and pages from Search Console, then upload both files.</p>
<h3>Prompt 2: Find the opportunities</h3>
<pre><code>I have uploaded two Search Console exports for the last 90 days: queries.csv and pages.csv.

Find:
1. Queries ranking between positions 4 and 15 with at least 50 impressions. List the top 20 by impressions, with the page that ranks for each.
2. Pages with at least 500 impressions and a click-through rate under 2 percent. These usually need a better title or description.
3. Queries where two or more of my pages compete for the same search (cannibalization).

Output three tables with these columns: query or page, page, position, impressions, clicks, CTR, suggested action.
Then list the five actions you would do first, and why.</code></pre>

<div class="note"><strong>Tip:</strong> compare like with like. Use the same date range for every export, or the trends will mislead you.</div>

<h2>Step 3: Fix titles and descriptions</h2>
<p>Pages on the second results page, or pages with plenty of impressions and few clicks, often need better wording rather than new content.</p>
<h3>Prompt 3: Rewrite titles and descriptions</h3>
<pre><code>For each page below, write three title options under 60 characters and three meta descriptions under 155 characters.

Each title and description must:
- include the main query naturally,
- state one concrete benefit,
- differ clearly from the other options.

Recommend one option per page and explain the choice in one sentence.

Pages (URL, current title, current description, main query):
[paste 10 rows]</code></pre>

<h2>Step 4: Run a technical audit</h2>
<p>Crawl your site, export the results and let Claude group the issues by how much they matter.</p>
<h3>Prompt 4: Technical audit from a crawl export</h3>
<pre><code>Here is a crawl export of my site (columns: URL, status code, title, meta description, H1 count, canonical, indexability, word count, internal links in, response time). I have uploaded it as crawl.csv.

Group the issues into three levels:
- Critical: pages blocked from indexing, server errors, redirect chains of two or more hops, noindex tags on money pages.
- Important: broken internal links, missing or duplicate titles, more than one H1, missing canonical tags.
- Minor: short descriptions, thin pages under 300 words.

For each level, list the affected URLs and the exact fix. Mark any issue you think may be a false positive.</code></pre>

<h2>Step 5: Build internal links and schema</h2>
<p>Internal links tell search engines which pages matter. Structured data tells them what those pages are.</p>
<h3>Prompt 5: Fix orphan pages and weak internal links</h3>
<pre><code>Using crawl.csv and this list of money pages: [paste list]

Find:
- orphan pages, meaning pages with zero internal links pointing to them,
- money pages with fewer than three internal links.

For each one, suggest two or three source pages that should link to it. Give the anchor text and the exact sentence to add. Do not add more than five links to any source page.</code></pre>

<h3>Prompt 6: Generate structured data</h3>
<pre><code>Write valid JSON-LD structured data for my site using only the facts below. If a field is unknown, leave it out. Do not invent details.

Business facts: [name, address, phone, founding year, service areas, social profiles]

Produce:
1. Organization and LocalBusiness markup for the homepage.
2. Service markup for each service page: [list services].
3. Article markup with author for each blog post.
4. FAQPage markup for pages that have a real FAQ section.

Output one script block per page type. Then give me a checklist for validating each block in Google's Rich Results Test.</code></pre>

<div class="note warn"><strong>Check the output.</strong> Structured data that describes things the page does not show, such as reviews or prices, can violate search guidelines. Only mark up what is visible to readers.</div>

<h2>Step 6: Plan content from real gaps</h2>
<p>Content gaps are topics your competitors cover and you do not. Turn them into briefs your writers can follow.</p>
<h3>Prompt 7: Content briefs from a keyword gap list</h3>
<pre><code>Here are 30 keywords where my competitors rank and my site does not. The file gaps.csv includes volume and difficulty from my keyword tool.

Group them into three intent types:
- problem-aware (the person has a problem but no solution yet),
- comparing options,
- ready to hire.

For the top ten in each group, write a content brief with:
- target query and search intent in one line,
- recommended title and URL slug,
- an H2 outline of five to seven questions,
- facts and sources I must include,
- internal links to add,
- the call to action.</code></pre>

<h3>Prompt 8: Location page outline</h3>
<pre><code>Create a location page outline for [service] in [city]. Use only the local details below.

Local details: [neighborhoods served, landmarks, typical jobs, service hours, licenses]

Include:
- a title under 60 characters,
- a meta description under 155 characters,
- one H1,
- a 100-word opening that addresses an urgent local problem,
- a short section on what the job includes,
- three local FAQ questions,
- a call to action.

Flag any detail you need from me. Do not invent reviews, statistics or testimonials.</code></pre>

<h2>Step 7: Strengthen local visibility</h2>
<p>For local businesses, your Business Profile is often the first thing a customer sees. Keep its categories, services and replies accurate and specific.</p>
<h3>Prompt 9: Review and profile audit</h3>
<pre><code>I have pasted my Business Profile categories, services list and the last 30 reviews below.

Tell me:
1. Which primary or secondary categories I may be missing for these services.
2. Which services have no description, or a weak one.
3. Which replies are generic and need a specific detail.
4. Three reply templates (positive, neutral, negative). Each thanks the reviewer for a specific detail from their review and stays under 70 words.

Do not write replies that offer incentives for reviews. Do not invent details the reviewer did not mention.

[paste data]</code></pre>

<h2>Step 8: Compare competitors and find link opportunities</h2>
<p>Competitor analysis shows where you are behind. Link prospecting shows where you can earn trust.</p>
<h3>Prompt 10: Competitor page comparison</h3>
<pre><code>Compare my homepage and service pages with these three competitor pages. Text is pasted below for each page.

Build a table with these rows: topics covered, proof offered (case studies, numbers, certifications), trust signals, calls to action, and approximate length.

Then list:
- the three areas where a competitor is clearly stronger,
- the one area where I could be the most useful.

Base your answer only on the text I provide.

[paste text for my pages and competitor pages]</code></pre>

<h3>Prompt 11: Link prospect list</h3>
<pre><code>Here are sites that link to my main competitor, with my notes on each (file prospects.csv).

Sort them into: resource pages, local associations, industry publications, and sponsor or partner pages.

For the top ten, suggest:
- one angle I could pitch, in one sentence,
- the asset I would offer,
- a personalized outreach email under 90 words.

Do not suggest buying links, using link networks or exchanging links at scale.</code></pre>

<h2>Step 9: Refresh content that is losing clicks</h2>
<p>Older articles often slip as competitors publish better answers. A focused refresh is faster than starting over.</p>
<h3>Prompt 12: Content refresh plan</h3>
<pre><code>This article has lost clicks over the last quarter: [URL, title, last updated date, query data].

Compare it against the top three current results for its main query. Summarize each one in a few lines first, then:
- list what they cover that this article misses,
- list facts that are out of date and need a current source,
- list the sections to rewrite or expand,
- give a word count target for each section.

Output an update plan. Do not rewrite the whole article.</code></pre>

<h2>Step 10: Report monthly</h2>
<p>A short, honest report keeps the team focused on what changed and what to do next.</p>
<h3>Prompt 13: Monthly SEO report</h3>
<pre><code>Using the exports below (Search Console clicks, impressions and average position for the last 28 days and the previous 28 days, plus top pages and top queries), write a one-page report.

Include:
- three wins,
- three problems,
- one next action,
- a table of the five largest changes, with a plain-English explanation of each.

If the data is too thin to draw a conclusion, say so. Do not claim cause and effect unless the data shows it.

[paste exports]</code></pre>

<h2>The complete SEO checklist</h2>
<p>Run through this list each month. Claude can help with most items, but the checks marked with a person are yours to confirm.</p>
<h3>Technical</h3>
<ul>
  <li>No important pages blocked from indexing. <em>(Confirm the robots file and noindex tags yourself.)</em></li>
  <li>No server errors on key pages.</li>
  <li>Redirect chains reduced to one hop.</li>
  <li>Canonical tags point to the preferred version of each page.</li>
  <li>Sitemap updated and submitted in Search Console.</li>
  <li>Key pages load quickly on mobile. <em>(Test one page by hand.)</em></li>
</ul>
<h3>On-page</h3>
<ul>
  <li>One clear H1 on each page.</li>
  <li>Unique titles under 60 characters.</li>
  <li>Unique descriptions under 155 characters.</li>
  <li>Images have descriptive alt text.</li>
  <li>The main answer appears in the first 100 words.</li>
</ul>
<h3>Content</h3>
<ul>
  <li>Every new article has a brief, a named author and a clear next step.</li>
  <li>Facts are traced to sources, and sources are dated.</li>
  <li>Top pages refreshed at least every six to twelve months.</li>
  <li>Thin pages either expanded, merged or removed.</li>
</ul>
<h3>Internal links and structure</h3>
<ul>
  <li>No orphan pages.</li>
  <li>Money pages have at least three relevant internal links.</li>
  <li>Topic clusters link to their pillar page and to each other.</li>
</ul>
<h3>Local (if you serve a local area)</h3>
<ul>
  <li>Business categories and services match what you actually offer. <em>(Confirm this in the profile yourself.)</em></li>
  <li>Business name, address and phone match across directories.</li>
  <li>Reviews answered within a few days, with specific replies.</li>
  <li>Photos and posts added on a steady schedule.</li>
</ul>
<h3>Authority</h3>
<ul>
  <li>New relevant links reviewed for quality, not just count.</li>
  <li>Any paid or sponsored links are labeled correctly.</li>
  <li>Brand mentions and citations checked for accuracy.</li>
</ul>
<h3>Measurement</h3>
<ul>
  <li>Monthly report covers clicks, impressions, position, calls or inquiries.</li>
  <li>Conversions tracked and checked against leads received.</li>
  <li>One action chosen for the next month and assigned to a person.</li>
</ul>

<h2>How do you make it automatic?</h2>
<p>Full automation is possible, but the sensible version automates analysis and keeps publishing human. A practical setup looks like this:</p>
<ol>
  <li><strong>Schedule the exports.</strong> Set a monthly reminder, or use the Search Console API to save exports to a folder.</li>
  <li><strong>Run the prompts in a saved project.</strong> Keep the business context and prompt library in one place so the outputs stay consistent.</li>
  <li><strong>Review and approve.</strong> A person checks each recommendation against the data before anything changes.</li>
  <li><strong>Track the results.</strong> Save each month's report so you can compare the trend over quarters.</li>
</ol>
<div class="note"><strong>Rule of thumb:</strong> automate what is read-only, such as analysis, drafts and reports. Keep anything that changes a live page behind an approval step.</div>

<h2>What guardrails should you use?</h2>
<ul>
  <li><strong>Verify every number</strong> against the original export before you act on it.</li>
  <li><strong>Never invent</strong> reviews, statistics, awards, testimonials or client names.</li>
  <li><strong>Respect site terms.</strong> Do not scrape review sites or competitor pages at scale in ways their terms forbid.</li>
  <li><strong>No manipulation.</strong> Do not use Claude to generate fake reviews, spam directories or link networks.</li>
  <li><strong>Disclose AI assistance</strong> where readers would expect it, and keep a named human accountable for every published page.</li>
</ul>

<h2>Common mistakes to avoid</h2>
<table>
  <thead><tr><th>Mistake</th><th>What happens</th><th>Better approach</th></tr></thead>
  <tbody>
    <tr><td>Running prompts without context</td><td>Generic advice that does not fit your business</td><td>Load the business context first</td></tr>
    <tr><td>Mixing date ranges</td><td>Trends that look real but are not</td><td>Use the same range for every export</td></tr>
    <tr><td>Publishing every suggestion</td><td>Over-optimized pages and lost quality</td><td>Choose the top three changes per month</td></tr>
    <tr><td>Trusting the first answer</td><td>Errors in titles, facts or schema</td><td>Ask for a second check and verify sources</td></tr>
    <tr><td>Skipping the measurement step</td><td>No way to tell what worked</td><td>Record each change and its date</td></tr>
  </tbody>
</table>

<h2>What should you do this week?</h2>
<ol>
  <li>Write your business context and save it as the first message in a project.</li>
  <li>Export 90 days of Search Console data and run Prompt 2.</li>
  <li>Pick ten pages from the results and run Prompt 3.</li>
  <li>Schedule the next monthly review in your calendar.</li>
</ol>

<h2>Need a team to run this for you?</h2>
<p>Our <a href="/#services">AI-focused SEO service</a> runs this kind of workflow with a person reviewing every change. We start with a free <a href="/#contact">growth audit</a> that shows where your biggest gaps are.</p>
<p>For more on the foundations, read our guides to <a href="/blog/what-is-ai-seo-and-how-to-do-it/">AI SEO</a>, <a href="/blog/ethical-link-building-guide/">ethical link building</a> and <a href="/blog/website-launch-marketing-checklist/">the website launch checklist</a>.</p>
""",
    faqs=[
        ("Can Claude check my Google rankings by itself?",
         "Not unless you give it data or connect a tool you have authorized. Export your Search Console data and upload it, then Claude can analyze it."),
        ("Is it safe to let AI change my website automatically?",
         "It is safer to automate analysis and drafts, and keep a person approving any change to a live page."),
        ("How often should I run these prompts?",
         "Run the performance analysis and reporting monthly. Run the technical audit after major site changes and at least quarterly."),
    ],
)

RELATED = [
    "what-is-ai-seo-and-how-to-do-it",
    "best-ai-tools-for-content-marketing",
    "website-launch-marketing-checklist",
]

# Existing article that should link to this one, so the cluster is connected both ways.
RELATED_UPDATES = {
    "what-is-ai-seo-and-how-to-do-it": ["how-to-automate-seo-with-claude", "how-to-get-cited-by-chatgpt-claude-and-perplexity", "content-marketing-strategy-step-by-step", "how-long-does-seo-take"],
}
