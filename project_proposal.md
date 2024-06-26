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

- [Predicting choice behaviour in economic games using gaze data encoded as scanpath images](https://pubmed.ncbi.nlm.nih.gov/36959330/)[1]

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

- [Eye Movements in Strategic Choice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4959529/)[2]

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

- [Complexity, Attention, and Choice in Games Under Time Constraints: A Process Analysis](https://psycnet.apa.org/fulltext/2018-43611-001.pdf?auth_token=f7f4cc5a510c0e2bdeeff4aa3156b8e34ecf74b4&returnUrl=https%3A%2F%2Fpsycnet.apa.org%2Frecord%2F2018-43611-001)[3]

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

- [Multiagent Narrative Experience Management as Story Graph Pruning](https://cdn.aaai.org/ojs/5229/5229-52-8327-1-10-20190920.pdf)[4]

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

- [Storyplaying : Agency and Narrative in Video Games](https://www.academia.edu/103929468/Storyplaying_Agency_and_Narrative_in_Video_Games)[5]

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

- [Strategic gaze: an interactive eye‑tracking study](https://www.proquest.com/docview/2500691599?accountid=8268&pq-origsite=Summon&parentSessionId=dvKX%2FlqTFnjhOWlURdGNm44oAJKN%2FhGH9YV3tOrjpc8%3D&sourcetype=Scholarly%20Journals)[6]

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

- [Error detection through mouse movement in an online adaptive learning environment](https://onlinelibrary.wiley.com/doi/10.1111/jcal.12483)[7]

Summary: Unlike the above studies, this looks into mouse
movement. Here, it is used to look at learning games, to
assess the potential other options a student was considering
on any given problem, which may help reveal where some
difficulty lay. It was found that it was better for lower
level students with simpler problems.

This strongly relates to this work as it implements mouse
tracking, though in a different environment. It provides
some framework for what this work is.

- [Unconscious Frustration: Dynamically Assessing User Experience using Eye and Mouse Tracking](https://dl.acm.org/doi/10.1145/3591137)[8]

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

- [Scoping Review of Bioelectrical Signals Uses in Videogames for Evaluation Purposes](https://ieeexplore.ieee.org/document/9913957)[9]

Summary: This paper is a collection and a review of works
done in the investigation of biolectrical signals and how
that relates to video game players. Specifically, the
authors find correlation between these signals and the
activity being performed.

This is a looser connection to the work here, in that it
is focused on the biology side of things, but it is a study
of user interaction with games, and therefore still
somewhat relevant here.

- [Does exposure to alternative decision rules change gaze patterns and behavioral strategies in games?](https://link.springer.com/article/10.1007/s40881-019-00066-0)[10]

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

Example game pages:

![First Game Page](images/game_pg1.PNG)

![Second Game Page](images/game_pg2.PNG)

## Preliminary Results and Outcomes

The artifact currently demonstrates the potential
viability of the `pygame` module in the completion
of parts one and two of the proposed project. Currently,
it has only been tested on a Windows OS. It
also collects a small portion of preliminary data
as part of that, indicating the potential executions
of part three of the proposed project. The results
are contained in the `json` files in the
`src/mousetracker/data` folder, minus the `data.json`
file that exists to show the initial draft of the
prototype's output. Overall, the results are mostly
the viability of the project, though the work
on the artifact has indicated that though `pygame`
is suitable for building a mouse tracker, it is
less so for building a narrative game, indicating
that it will likely have to be built in a different
system.

Current terminal output example:

![Example Ouput](images/example_output.PNG)


## Conclusions and Future Work

The current work done on this artifact is a small
glimpse into the work required to realize the full
project proposed here. It is merely a first draft,
much, if not all of it likely to be absent in the final
work. There would have to be a reevaluation of the language
and/or tool in which it is built, for example, as `pygame`
is limited in functionality that facilitates building a
narrative choice game. Referencing works on `itch.io` will
help in the further research in this aspect. However the
project then moves forward, the mouse tracker will have to
either be extricated from the game and made to work as
a separate program run on it, or part one becomes entwined
with part two, reducing the versatility of that part of the
tool but managing scope and workload to ensure the project
is completable. From there, the data analysis section would
be created to assess correlations and relationships between
data regarding time and mouse placement collected.

Provided that part one remains separate from part two, the
primary ethical concern is the potential for the mouse
tracker to be implemented without the awareness of players
on other games built in the same system as part two. The
separation that would benefit broader use would also be
the element that risks abuse. There is also the fact that
the data collection does require human trials, which will
have to go through review from an ethics board before it
can be completed.

## References

[1] Sean Anthony Byrne et al. 2023. Predicting choice behaviour in economic games using gaze data encoded as scanpath images. *Scientific reports* vol. 13,1 4722. doi:10.1038/s41598-023-31536-5

[2] Neil Stewart et al. 2015. Eye Movements in Strategic Choice. *Journal of behavioral decision making* vol. 29,2-3 : 137-156. doi:10.1002/bdm.1901

[3] L. Spiliopoulos, A. Ortmann, and L. Zhang. 2018. Complexity, attention, and choice in games under time constraints: A process analysis. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 44(10), 1609–1640. https://doi.org/10.1037/xlm0000535

[4] Stephen G. Ware, Edward T. Garcia, Alireza Shirvani, and Rachelyn Farrell. 2019. Multi-Agent Narrative Experience Management as Story Graph Pruning. IEEE Transactions on Games. https://doi.org/10.1109/TG.2022.3177125

[5] Sebastian Domsch. 2013. *Storyplaying: Agency and Narrative in Video Games*. De Gruyter.

[6] J. Hausfeld, K. von Hesler, and S. Goldlücke. 2021. Strategic Gaze: An Interactive Eye-Tracking Study. *Experimental Economics* 24, no. 1 : 177-205. https://doi.org/10.1007/s10683-020-09655-x.

[7] Susanne M. M. de Mooij, Maartje E. J. Raijmakers, Iroise Dumontheil, Natasha Z. Kirkham, and Han L. J. van der Maas. 2020. Error detection through mouse movement in an online adaptive learning environment. *J Comput Assist Learn*. 37: 242–252. https://doi.org/10.1111/jcal.12483

[8] Scott A. Stone and Craig S. Chapman. 2023. Unconscious Frustration: Dynamically Assessing User Experience using Eye and Mouse Tracking. Proc. ACM Hum.-Comput. Interact. 7, ETRA, Article 168 (May 2023), 17 pages. https://doi.org/10.1145/3591137

[9] A. Calvo-Morata, M. Freire, I. Martínez-Ortiz and B. Fernández-Manjón. 2022. Scoping Review of Bioelectrical Signals Uses in Videogames for Evaluation Purposes. IEEE Access, vol. 10, pp. 107703-107715. doi: 10.1109/ACCESS.2022.3213070.

[10] J. Zonca, G. Coricelli, and L. Polonio. 2019. Does exposure to alternative decision rules change gaze patterns and behavioral strategies in games?. J Econ Sci Assoc 5, 14–25. https://doi.org/10.1007/s40881-019-00066-0
