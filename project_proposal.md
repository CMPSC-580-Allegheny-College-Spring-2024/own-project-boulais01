# Junior Seminar (CMPSC 580) Project Proposal

## Semester: Spring 2024

## GitHub Handle: boulais01

## Name: Mordred Boulais

## Major: Former CS Major

## Project Title: Choice Analysis Through Mouse Movement Data 

---

## Introduction

TODO: Introduce the proposed project, providing a concise summary of the project goals, its key elements, offering the reader a quick understanding of the research's scope. The section continues to outline the main topics, research questions, hypotheses, and /or theories in a clear and meaningful language to provide a type of roadmap for the reader to navigate the forthcoming details of the project. This section also needs to motivate the project by providing context for the study, outlining the current state of knowledge in the field, and highlighting any gaps or limitations in existing research. The section serves as a foundational guide that enables the reader to grasp the context of the study, in addition to its structure, before moving into a more technically-based discussion in the following sections of the article. In short, the "Introduction" section needs to answer the `what` and `why` questions, that is `what is the project?` and `why is the project important?`

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

## Literature Review

TODO (10 source minimum, with 5 of those being published peer-reviewed articles): Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further (in detail) contributes to the `why is the project important?` question.

Articles:

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
study. 

- [Eye Movements in Strategic Choice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4959529/)

- [Complexity, Attention, and Choice in Games Under Time Constraints: A Process Analysis](https://psycnet.apa.org/fulltext/2018-43611-001.pdf?auth_token=f7f4cc5a510c0e2bdeeff4aa3156b8e34ecf74b4&returnUrl=https%3A%2F%2Fpsycnet.apa.org%2Frecord%2F2018-43611-001)

- [Multiagent Narrative Experience Management as Story Graph Pruning](https://allegheny.summon.serialssolutions.com/#!/search/document?ho=t&include.ft.matches=f&fvf=ContentType,Journal%20Article,f%7CContentType,Paper,f%7CContentType,Book%20%2F%20eBook,f%7CSubjectTerms,game%20theory,f%7CSubjectTerms,computer%20science,f%7CSubjectTerms,computer%20science%20and%20game%20theory,f%7CLanguage,English,f%7CSubjectTerms,choice%20behavior,f%7CSubjectTerms,science%20%26%20technology,f%7CDiscipline,computer%20science,f%7CSubjectTerms,computer%20science%5C,%20information%20systems,f%7CSubjectTerms,computer%20science%5C,%20interdisciplinary%20applications,f&l=en&searchscope=All&q=(choice)%20AND%20(narrative%20game)&id=FETCHMERGED-LOGICAL-c207t-6cce8e1343725519f4918b4ee2e60170ac905accddb2ed1f953689e25d79132c2)

- [Storyplaying : Agency and Narrative in Video Games](https://web.p.ebscohost.com/ehost/detail/detail?vid=3&sid=c603769a-90c7-4ab7-9191-f57721409754%40redis&bdata=JkF1dGhUeXBlPWlwLHNoaWImc2l0ZT1laG9zdC1saXZl#db=e000xna&AN=641742)

## Prototype

TODO: Discuss the methods of the project to be able to answer the `how` question (`how was this project completed?`). For this section, you must describe  the methodology behind your implemented prototype. The methods section in an academic research outlines the specific procedures, techniques, and methodologies employed to conduct the study, offering a transparent and replicable framework for the research. It details the resources behind the work, in terms of, for example, the design of the algorithm and the experiment(s), data collection methods, applied software libraries, required tools, the types of statistical analyses and models which are applied to ensure the rigor and validity of the study. This section provides clarity for other researchers to understand and potentially replicate the study, contributing to the overall reliability and credibility of the research findings.

## Preliminary Results and Outcomes

TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact

## Conclusions and Future Work

TODO: Summarize your work and outline future steps needed to complete to take the project to the next stage (for example, if you were to continue with this project in 600/610). You must also address ethical implications of your project, especially as pertains to the public release or use of your software or methods.

## References

TODO: Add references in the [ACM style](https://www.acm.org/publications/authors/reference-formatting). All references must be cited in the proposal.
