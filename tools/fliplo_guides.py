"""Fliplo guides: search-targeted how-tos that live under /fliplo/guides/.

Copy rule: no long dashes. Only describe things the app really does.
"""

GUIDES = [
    {
        "slug": "make-a-gif-on-iphone",
        "title": "How to make a GIF on your iPhone",
        "desc": "Draw your own animated GIF on iPhone or iPad, frame by frame, and share it to Messages, social apps or Photos. A step by step guide using Fliplo.",
        "teaser": "Draw a few frames, press play, share a looping GIF.",
        "body": """
<p>You do not need a computer to make an animated GIF. A GIF is just a short loop of drawings shown one after another, and your iPhone or iPad is enough to draw them. This guide uses Fliplo, a free frame-by-frame animation app, but the ideas work in any animation tool.</p>

<h2>1. Start with a tiny idea</h2>
<p>Pick something that moves in a loop: a bouncing ball, a blinking eye, a waving hand, a spinning star. Loops are forgiving, because the last frame leads back to the first and the motion feels endless.</p>

<h2>2. Create a project</h2>
<p>Open Fliplo and start a new project. A square canvas works well for chat apps and social posts. Twelve frames per second is a good default: smooth enough to read as motion, light enough that you only draw a few pictures per second of animation.</p>

<h2>3. Draw your first frame</h2>
<p>Use the pencil, brush or marker with Apple Pencil or your finger. Keep the first drawing simple. Every extra detail is something you have to redraw on every frame.</p>

<h2>4. Add the next frame and use onion skin</h2>
<p>Tap <strong>Add Frame</strong>. Onion skin shows a faint copy of the neighbouring frames, so you can see where the ball was and move it a little. Small changes between frames make smooth motion. Big jumps make it look jumpy.</p>

<h2>5. Press play</h2>
<p>Play the animation often, not just at the end. If a part looks wrong, go back and fix that one frame. You can also hold a frame for longer to slow a moment down, or change the playback speed while you test.</p>

<h2>6. Export the GIF</h2>
<p>Tap the share icon and choose <strong>GIF</strong>. You can export at 100%, 50% or 25% size. Smaller files send faster in messaging apps. When it finishes, share it straight to Messages, WhatsApp, Instagram or any other app, or save it to Photos. Free exports carry a small "Made with Fliplo" mark. Fliplo Pro removes it and adds MP4 export.</p>

<h2>Tips for a good first GIF</h2>
<ul>
<li>Aim for 8 to 16 frames. You can always add more later.</li>
<li>Make the last frame almost match the first one so the loop is seamless.</li>
<li>Keep the background plain so the file stays small.</li>
<li>Use a bold, simple style. Thick lines read clearly on a small screen.</li>
</ul>
""",
        "faqs": [
            ("Can I make a GIF on iPhone for free?", "Yes. Fliplo is free to download and lets you draw up to 48 frames and export a GIF. Free GIFs include a small watermark."),
            ("How many frames does a GIF need?", "As few as two. A short loop of 8 to 16 frames at 12 frames per second is a good starting point."),
            ("Does it work on iPad with Apple Pencil?", "Yes. Fliplo runs on iPhone and iPad and supports Apple Pencil pressure."),
        ],
    },
    {
        "slug": "onion-skinning-explained",
        "title": "Onion skinning explained for beginners",
        "desc": "What onion skinning is, why animators use it, and how to use it to draw smooth frame-by-frame animation on iPhone and iPad.",
        "teaser": "See the frames around the one you are drawing.",
        "body": """
<p>Onion skinning is the single most useful trick in frame-by-frame animation. It shows faint copies of the frames before and after the one you are drawing, so you can see how your picture needs to change.</p>

<h2>Where the name comes from</h2>
<p>Traditional animators drew on thin paper over a light table. Because the paper was almost see-through, they could see the previous drawing underneath, like the layers of an onion skin. Digital apps copy that idea.</p>

<h2>Why it matters</h2>
<p>Motion is about spacing. If a ball moves 10 pixels between frames, it looks slow. If it moves 80, it looks fast. Without onion skin you are guessing. With it, you can place each new drawing a precise step away from the last one.</p>

<h2>How to use it in Fliplo</h2>
<ol>
<li>Draw your first frame.</li>
<li>Add a new frame. The previous drawing appears as a faint ghost.</li>
<li>Draw the next position over the ghost, nudged in the direction of the motion.</li>
<li>Repeat. Play back often.</li>
</ol>
<p>Fliplo lets you choose how many frames to show before and after, up to 5 each way, and change the colours. Use different colours for before and after so you can tell at a glance which way time is going.</p>

<h2>How many frames should you show?</h2>
<ul>
<li><strong>One before:</strong> the simplest set up and good for most beginner work.</li>
<li><strong>Two or three before and one after:</strong> useful for arcs and bounces, where you want to see where the motion is heading.</li>
<li><strong>Five each way:</strong> handy for slow, smooth movement such as a drifting cloud, but it can get cluttered on a small screen.</li>
</ul>

<h2>Common mistakes</h2>
<ul>
<li>Tracing the ghost exactly, which makes nothing move. Change it a little each time.</li>
<li>Making the steps too big. Start small and speed up.</li>
<li>Forgetting to turn it off to check the final look. Onion skin is a guide, not part of the picture.</li>
</ul>
""",
        "faqs": [
            ("Is onion skinning only for digital animation?", "No. It comes from traditional animation on thin paper over a light table. Digital apps make it automatic."),
            ("Does onion skin show up in my exported GIF?", "No. It is only a drawing guide and never appears in exports."),
        ],
    },
    {
        "slug": "animate-a-bouncing-ball",
        "title": "Animate a bouncing ball in 12 frames",
        "desc": "A classic first animation exercise: a bouncing ball in 12 frames. Learn spacing, squash and stretch and looping on iPhone or iPad.",
        "teaser": "The classic first animation, step by step.",
        "body": """
<p>The bouncing ball is the first exercise in almost every animation course. It teaches timing, spacing and weight with the simplest possible subject. Fliplo even includes a Bouncing Ball template, but it is worth drawing your own once.</p>

<h2>The plan: 12 frames</h2>
<p>At 12 frames per second, 12 frames is exactly one second. We will make the ball fall, hit the ground, squash, and rise again. The loop then repeats.</p>

<h2>Step by step</h2>
<ol>
<li><strong>Frame 1:</strong> draw the ball at the top of its bounce. This is the slowest moment, since it is changing direction.</li>
<li><strong>Frames 2 to 4:</strong> the ball falls. Space the drawings further apart each time, because gravity makes it accelerate.</li>
<li><strong>Frame 5:</strong> the ball touches the ground. Draw it slightly flattened.</li>
<li><strong>Frame 6:</strong> the biggest squash. Wider and shorter, with the same overall area.</li>
<li><strong>Frame 7:</strong> the ball stretches upward as it leaves the ground.</li>
<li><strong>Frames 8 to 11:</strong> the ball rises. The spacing gets smaller as it slows down.</li>
<li><strong>Frame 12:</strong> back near the top. It should lead smoothly into frame 1.</li>
</ol>

<h2>Spacing is the secret</h2>
<p>Fast motion has big gaps between drawings. Slow motion has small gaps. Near the top of the bounce, put the drawings close together. Near the ground, spread them out. This one idea does more for believable movement than any amount of detail.</p>

<h2>Squash and stretch</h2>
<p>A real rubber ball deforms when it hits something. Drawing a flatter ball on impact and a slightly taller one as it speeds up gives it weight. Keep the volume roughly the same: if it gets wider, make it shorter.</p>

<h2>Use hold durations for impact</h2>
<p>Holding the impact frame a little longer can make the hit feel heavier. In Fliplo you can set a hold duration per frame, and both the preview and your exported GIF or MP4 follow it.</p>

<h2>Next steps</h2>
<ul>
<li>Add a shadow that gets smaller as the ball rises.</li>
<li>Make each bounce lower than the last, then let it roll to a stop.</li>
<li>Try a heavier ball, such as a bowling ball, with less squash and fewer bounces.</li>
</ul>
""",
        "faqs": [
            ("How many frames does a bouncing ball need?", "Twelve frames at 12 frames per second makes a one second bounce, which is a good starting exercise."),
            ("What is squash and stretch?", "It is the way objects deform when they move or hit something. It makes drawn motion feel alive and weighty."),
        ],
    },
    {
        "slug": "flipbook-animation-ideas-for-kids",
        "title": "Flipbook animation ideas for kids",
        "desc": "Twelve simple animation ideas for kids to draw on an iPad or iPhone, from a growing flower to a bouncing ball, plus tips for getting started.",
        "teaser": "Twelve ideas that fit in a handful of frames.",
        "body": """
<p>Kids love flipbooks because the magic is instant: draw a few pictures, flick through them and the drawing moves. You can do the same on a tablet. Here are twelve ideas that need only a handful of frames, and some tips for helping young animators get started.</p>

<h2>Twelve ideas that work in 6 to 12 frames</h2>
<ol>
<li><strong>A bouncing ball.</strong> The classic first animation.</li>
<li><strong>A growing flower.</strong> A seed, a stem, a bloom.</li>
<li><strong>A blinking eye.</strong> Open, half, closed, half, open.</li>
<li><strong>A walking stick figure.</strong> Four poses are enough for a loop.</li>
<li><strong>A balloon floating up.</strong> Move it a little higher each frame.</li>
<li><strong>A setting sun.</strong> Slowly lower it behind a hill.</li>
<li><strong>A waving hand.</strong> Rock it left and right.</li>
<li><strong>A rolling wheel.</strong> Draw a mark on it so the spin is visible.</li>
<li><strong>A raindrop splash.</strong> Falling, hitting, spreading rings.</li>
<li><strong>A character changing expression.</strong> Happy to surprised to happy.</li>
<li><strong>A fish swimming across the screen.</strong> Add bubbles.</li>
<li><strong>A name that draws itself.</strong> Add a few more strokes each frame.</li>
</ol>

<h2>Tips for helping kids get started</h2>
<ul>
<li><strong>Start tiny.</strong> Six frames finished is better than sixty abandoned.</li>
<li><strong>Use onion skin.</strong> Seeing the previous drawing shows kids exactly how far to move things.</li>
<li><strong>Play it back early and often.</strong> Seeing a drawing move is the reward.</li>
<li><strong>Use big, bold lines.</strong> They are easier to draw and easier to see.</li>
<li><strong>Duplicate frames.</strong> Copy a frame, then change just the part that moves.</li>
<li><strong>Make mistakes easy to fix.</strong> Fliplo has a friendly "Oops" undo button right on the canvas.</li>
</ul>

<h2>Sharing the result</h2>
<p>When the animation is ready, export it as a GIF and share it with family. Or save it to Photos and play it on a bigger screen.</p>

<h2>Privacy</h2>
<p>Fliplo collects no personal data, has no accounts and no ads. Drawings stay on the device unless you choose to share them.</p>
""",
        "faqs": [
            ("What age is Fliplo for?", "It is rated 4+ and designed to be easy for beginners and kids, with large tap targets and a one tap undo."),
            ("Does Fliplo have ads?", "No. Fliplo has no ads and collects no personal data."),
        ],
    },
]
