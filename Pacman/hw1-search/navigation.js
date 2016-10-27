
/** This is a really hacky way to load the navigation bar to the main html pages **/

var navbar = 
// First, draw the logo image and the title
['<div id="head">',
'<div id="logo">',
'<a href="home.html"><img id="logo_img" src="images/AI_logo_transparent.png" alt="AI_logo" /></a>',
'</div>',
'<div id="title">',
'<h1>UC Berkeley CS188 Intro to AI -- Course Materials</h1>',
'</div>',
'</div>',

// Begin navigation list
'<ul id="list-nav">',

'<li><a href="home.html">Home</a></li>',
'<li><a href="course_schedule.html">Course Schedule</a></li>',

// Lecture Submenu
'<li><a href="lecture_videos.html">Lectures</a>',
'<ul>',
'<li><a href="lecture_videos.html">Videos</a></li>',
'<li><a href="lecture_slides.html">Slides</a></li>',
'</ul>',
'</li>',

// Homework Submenu
'<li><a href="homework.html">Homework</a>',
'<ul>',
'<li><a href="homework.html">Electronic Homework</a></li>',
'<li><a href="section_handouts.html">Section Handouts</a></li>',
'</ul>',
'</li>',

// Project Submenu
'<li><a href="project_overview.html">Pacman Projects</a>',
'<ul>',
"<li><a href='project_overview.html'>Overview</a></li>",
"<li><a href='project_instructions.html'>Instructor's Guide</a></li>",
"<li><a href='tutorial.html'>P0: UNIX/Python Tutorial</a></li>",
"<li><a href='search.html'>P1: Search</a></li>",
"<li><a href='multiagent.html'>P2: Multiagent Search</a></li>",
"<li><a href='reinforcement.html'>P3: Reinforcement Learning</a></li>",
"<li><a href='tracking.html'>P4: Ghostbusters</a></li>",
"<li><a href='classification.html'>P5: Classification</a></li>",
"<li><a href='contest.html'>Contest: Pacman Capture the Flag</a></li>",
"<li><a href='project_log.html'>Project Updates</a></li>",
'</ul>',
'</li>',

// Rest of navigation bar
'<li><a href="exams.html">Exams</a></li>',
//"<li><a href='students_guide.html'>Student's Guide</a></li>", include later

// Instructor's Guide Submenu
"<li><a href='instructors_guide.html'>Instructor's Guide</a>",
'<ul>',
"<li><a href='instructors_guide.html'>Overview</a>",
"<li><a href='course_policies.html'>Course Policies</a></li>",
"</ul>",
"</li>",

"<li><a href='students_guide.html'>Student's Guide</a></li>",

// More AI Courses Submenu
'<li><a href="more_courses_berkeley.html">More AI Courses</a>',
'<ul>',
'<li><a href="more_courses_berkeley.html">At Berkeley</a></li>',
'<li><a href="more_courses_other_schools.html">At Other Schools</a></li>',
'</ul>',
'</li>',

'<li><a href="contact.html">Contact</a></li>',
'</ul>'].join('');

document.write(navbar);
