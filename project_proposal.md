# Junior Seminar (CMPSC 580) Project Proposal

## Semester: Spring 2024

## GitHub Handle: boulais01

## Name: Mordred Boulais

## Major: Former CS Major

## Project Title: Choice Analysis Through Mouse Movement Data 

---

## Introduction

The proposed project is an analysis of several factors revolving around
decision-making in a narrative game. Specifically, this will analyze the time it
takes to make a choice alongside the placement of the mouse, and for what
durations, in that time frame. This is in conversation with gaze-tracking work
of a similar nature, though the focusses for those tend more tends economic or
ethical choices. There are not any studies published to the databases searched
that included this aspect of assesment, hence that being the focus of the
analysis here. The final project will consist of three sections; part one being
the mouse tracking module, part two being the narrative choice-based game, and
part three being the analysis of the data collected from a study of players
making choices tracked by part one during play of part two. The game and
tracking are planned to be implemented through use of the module
[`pygame`](https://www.pygame.org/docs/).
The demo included will be a sample draft of mouse movement tracking in a
`pygame` implementation.

## Literature Review

- [Predicting choice behaviour in economic games using gaze data encoded as scanpath images](https://pubmed.ncbi.nlm.nih.gov/36959330/)

Summary: This study uses scanpath images created from eye-tracking software
to investigate if the scanpath images increase the accuracy of choice
prediction. Specifically, the study aims to achieve a better awareness of
the uses of eye-tracking using their scanpath image generation to assess
choices made by participants in economic games. This is examined by
looking at which choice patterns the particpant uses(Equilibrium, Naive,
and Coordination) alongside the length of time for making such choices
and assessing these elements alongside the patterns displayed by the
scanpath images. Namely, these allow the researchers to assess the
likely thought process of the participant. Using machine learning,
the researchers classify each scanpath. This is how the model
predictions are assessed. Ultimately, this study was able to
represent the decision-making processes of the participants
through these scanpath images.

This relates to this project in that the goal is to use
mouse tracking in a similar way to the eye tracking in this
study. It also covers decision analysis, though in a manner
different than this project will be doing. 

- [Eye Movements in Strategic Choice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4959529/)

Summary: This study observes the eye movements of players in
strategic games, alongside existing reasoning models such as
level-*k* theories and attribute models. Level-*k* theories
studies the why of players make the choices they do. By
comparing the eye tracking information to these theories,
researchers could assess the correlations with each level. They
found that trained players had different eye movements than
untrained, and similar eye movements to each other. Another
model of comparison was attribute models, for risky,
multiattribute choices. Using a simple regression, the study
found that the attributes, attributes and fixations, and
transitions and attribute values had statistically
significant correlation. With these results it was determined
that the time and eye tracking data appeared most similar
to accumulator models.

Much like the previous article, this involves an analysis
of player choices using gaze tracking. This study also goes
in-depth about the theories of though that are associated
with choices and behaviors, and uses a regression to
analyze that. A future element of this project, the data
analysis, will likely incorporate a similar element.

- [Complexity, Attention, and Choice in Games Under Time Constraints: A Process Analysis](https://psycnet.apa.org/fulltext/2018-43611-001.pdf?auth_token=f7f4cc5a510c0e2bdeeff4aa3156b8e34ecf74b4&returnUrl=https%3A%2F%2Fpsycnet.apa.org%2Frecord%2F2018-43611-001)

Summary: This study utilizes level-*k* theory to look at
player choices in strategy games where another player is
involved, without knowing what choice the other player will
make. Using this framework, the researchers then manipulated
elements such as time and available information to assess
shifts in strategy. Overall, it is found that the hypothesis
of reduced time leading to reduced assessment of information
and time taken to make that decision, altering strategic
behavior from the baseline of the player.

This adds in the element of time constraints to some of the
theories discussed previously, and how that influences and
alters the positioning of player choices relative to these
theories. The study of choice is prevalent in the work being
done on this project as well.

- [Multiagent Narrative Experience Management as Story Graph Pruning](https://cdn.aaai.org/ojs/5229/5229-52-8327-1-10-20190920.pdf)

Summary: This study creates a story through a narrative where
the player and NPCs can take actions. In order to study
refining so that the player is not limited in actions, the
potential actions of the NPCs are limited instead.
Specifically, the story graph is pruned by ensuring there is
one action an NPC can take in any given possible situation.
This is in some ways limited by following a Markovian model
and by the small sample size. However, the results indicate
that the hypothesis that players will find the intelligent
story creation over the random is supported by the data
significantly enough to indicate that a larger sample size
will produce a similar end result.

This study is related to part two of this proposed project, as
it concerns itself with the construction of a narrative game.
It outlines the construction of an idealized game for a player.

- [Storyplaying : Agency and Narrative in Video Games](https://www.academia.edu/103929468/Storyplaying_Agency_and_Narrative_in_Video_Games)

(Focused on the `Introduction` and
`Choice and Narrative in Video Games` sections in the summary)

Summary: This study discusses Future Narratives, a nodal form
of storytelling similar to that seen in the study above. In
this, there is a node with multiple potential mutually exclusive
paths branching off of it, typically each being a node themself.
In defining a Narrative as anything that aids the
user/player/viewer in drawing connections between two or more
events. Overall, this study explores the definition of Future
Narratives in relation to video games. In doing so, it uses
the term *storyplaying*, which is to refer to something both
played as a game and read as a narrative. Overall, it is a
look at the agency of the player and the narrative created
in that.

This is relevant to the work here, as part two will be a
narrative game of a model similar to those described here;
something where the player's agency affects the narrative.

- [Strategic gaze: an interactive eye‑tracking study](https://www.proquest.com/docview/2500691599?accountid=8268&pq-origsite=Summon&parentSessionId=dvKX%2FlqTFnjhOWlURdGNm44oAJKN%2FhGH9YV3tOrjpc8%3D&sourcetype=Scholarly%20Journals)

Summary: In this study, researchers looked at how people
made strategic decisions when they could see their partner's
gaze path. This is in the same vein/in conversation with the
second two papers described here, with the added element of
awareness of the other person's gaze. Those in the group
who saw the gaze of their partner overall had better
results/more success than those that couldn't, with this
added layer of information allowing them to make more
strategic decisions.

Much of the relation to the work here is highlighted as
part of the mentioned studies above. Unlike the work here,
the interactive elements of the games here feature other
people.

- [Error detection through mouse movement in an online adaptive learning environment](https://onlinelibrary.wiley.com/doi/10.1111/jcal.12483)

Summary: Unlike the above studies, this looks into mouse
movement. Here, it is used to look at learning games, to
assess the potential other options a student was considering
on any given problem, which may help reveal where some
difficulty lay. It was found that it was better for lower
level students with simpler problems.

This strongly relates to this work as it implements mouse
tracking, though in a different environment. It provides
some framework for what this work is.

- [Unconscious Frustration: Dynamically Assessing User Experience using Eye and Mouse Tracking](https://dl.acm.org/doi/10.1145/3591137)

Summary: This study uses both eye and mouse tracking to
observe and analyze users and their experiences when
playing a game. Primarily, the efforts were put into
refining gaze tracking, as they had three implementations
in affect at once for each trial. With this, it researchers
identified page design elements that were more confusing
or frustrating to users.

This study is focused on UX, but implements both gaze
tracking and mouse tracking, instead of one or the other.
While this work will not use gaze tracking, the mouse
tracking element runs parallel to the goals and findings
of this study.

- [Scoping Review of Bioelectrical Signals Uses in Videogames for Evaluation Purposes](https://ieeexplore.ieee.org/document/9913957)

Summary: This paper is a collection and a review of works
done in the investigation of biolectrical signals and how
that relates to video game players. Specifically, the
authors find correlation between these signals and the
activity being performed.

This is a looser connection to the work here, in that it
is focused on the biology side of things, but it is a study
of user interaction with games, and therefore still
somewhat relevant here.

- [Does exposure to alternative decision rules change gaze patterns and behavioral strategies in games?](https://link.springer.com/article/10.1007/s40881-019-00066-0)

Summary: This is in conversation with other works
regarding eye tracking and strategy, looking to fill in
the gaps left in that research. Specifically, this paper
discusses where the analysis of level-*k* theory is not
taken, looking at the reasonings involved in the observed
thought processes.

This, as a continuation of other work discussed here,
is involved in the tracking and assessing player choices
aspect of this work.

## Prototype

Currently, the prototype is run from the command line,
where it executes the simple game created in `pygame`,
collects time, choice, and mouse location information,
and displays a limited form of that. Due to the nature
of the prototype, the data included in this
repository stems from testing the most recent
implementation of the tool, as well as the first `json`
created in an initial trial with an earlier draft of
the code. The data is collected using a wrapper to
collect time, and `yield` statements to collect the
state throughout the game as well as the choices made.
It is stored and displayed using a `json` file.
This project makes use of not only the `pygame` and
`json` modules, but also `typing`, `typer`, `rich`,
`datetime`, and `time`. All of these dependencies are
handled through `poetry` as outlined in the prototype
explanation in the `src` folder. As of yet, no data
processing is completed with the data.

## Preliminary Results and Outcomes

TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact

## Conclusions and Future Work

TODO: Summarize your work and outline future steps needed to complete to take the project to the next stage (for example, if you were to continue with this project in 600/610). You must also address ethical implications of your project, especially as pertains to the public release or use of your software or methods.

## References

TODO: Add references in the [ACM style](https://www.acm.org/publications/authors/reference-formatting). All references must be cited in the proposal.
