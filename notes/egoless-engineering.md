---
btime: 2025-04-17 08:14
layout: note.njk
mtime: 2025-05-08 08:09
permalink: notes/{{ page.fileSlug }}/index.html
status: draft
tags:
- developer
title: Egoless Engineering
---
I have drawn inspiration from Dan McKinley's slidedeck on a presentation about [Egoless Engineering](https://egoless.engineering/). 
He presents organizational pitfalls he found in software focused companies, what makes other engineering teams work well and how to get there.

Below are my notes from going through it. I have aimed to replicate Dan McKinley's message in the first chapter and added my follow-up thoughts and questions afterwards.

## Core challenge: Work distribution
Once you have two employees, you have to divide responsibilities. How is crucial and consequences are awful to contemplate. So most companies don't contemplate it that much.

Ironically, computer scientists are also really bad at it despite literally studying the asymptotic limits of work completion under various conditions:
- Amdahl's Law: Highlights that you can't just parallelize forever; coordination costs eventually dominate.
- Kingman's formula: Small growth in requests for a shared resource can have nonlinear implications for wait times as utilization increases.

## Negative patterns Dan has seen across companies
### Pattern 1: Tasks and job descriptions are conflated
For any new thing a company wants to do, a common tendency is to put up a new job description.
These days companies want to rub some AI onto their product and hire for new AI engineers, whilst AI-interested engineers already exist within the company.  
Releases need to be coordinated -> There should be release managers.  
We need JavaScript written -> Frontend engineers should do it.

### Pattern 2: The DevOps revolution is ... unevenly distributed
Divide persists mostly between SRE and development.  
Most companies claim they "do devops", but actually bridging the divide and building empathy between the two groups is rarely fully realized in practice.

### Pattern 3: Strict division of labor feels obvious, but is wrong, and also sucks
Once work is subdivided, they naturally try to arrange people into assembly lines. AI work goes to the AI person. Ops work goes to the ops person.

That seems obvious, but is believed to be wrong. The argument is, I believe, that this might lead to bottlenecks slowing it all down.

### Pattern 4: Bad organization is a radioactive source of extra work
Poorly factored organizational boundaries creates additional work. A security team to do the security tickets instead of weaving it into the regular dev work.

### Pattern 5: Humans have an impressive capacity for chauvinism
>[!Info]
>Chauvinism (in this context): The strong and unreasonable belief that your group is the best or most important.


There can be a general tendency to imagine other people's jobs are easy compared to ours.  
>We'll make the platform, you can worry about the _business logic_ (term of art implying "your bullshit") 

It is worrisome if platform teams are full of people who aren't worried about what the company they work for even does.

Brilliant jerks are poison. They cause strongest people to leave, or job hunt and slow their performance. Thus, reinforcing the jerk's statement, making them appear as a necessary evil.


## Common Theme: Parochialism & Ego
>[!info]
>Parochialism: A limited or narrow outlook, especially focused on a local area; narrow-mindedness.

The yin and yang of dysfunction.

|              | Positive Spin                                          | Negative Spin                                              |
| 



 | 

















 | 


















- |
| Parochialism | Deference, not wanting to step on someone else's toes. | Lack of curiosity.                                         |
| Ego          | Pride in your work                                     | Territoriality. Dismissiveness in the abilities of others. |

## A Happier Story
Tear down existing barriers between roles. Encourage everyone in engineering to be capable of working on a wider range of tasks. With that mindset and a stable devops acting as a force multiplier, the presenters engineering team had extra time which they used to...

### Empower Everybody Else
Presenter tells the story of how a designer broke prod. One option would have been to strip them from privileges. Instead the team gave them tools and privileges so they could fix it the next time.  Consequently, engineers got more free time from this designers independence. The engineers used it to build better monitoring and test suites enabling safer deployments for everyone.

### Domain experts, not domain owners
There are security experts who partner with the Dev Teams. The dev teams own their dev work, including its security aspects (unlike the scenario described in [[Egoless Engineering#Pattern 4 Bad organization is a radioactive source of extra work|Pattern 4]]).
The word for the idea that SRE and developers should share tasks is DevOps, but the principle applies to nearly all teams.

The expert differentiates from an owner as in wanting to make his discipline more accessible to others.

### Proactive cross-pollination
>[!Info]
>Pollination: the process in which pollen is taken from one plant to another so that new plant seeds can be produced

Understand your colleagues' work!  
New hire bootcamps, senior bootcamps (join other teams for a month), hack weeks. 

### Intentional team values
Elitism as an attitude is poison.

We are a team that
- digs ditches. Nobody is too good for any task.
- leaves things better than when found. Even if no one is watching.

## Live the movement
How can you be effective in the cultural change?  
Try to help, *genuinely*. 
- What if you took marketing seriously and tried to help them instead of just shitposting?
- Continuous delivery: turns out product developers actually love being empowered to fix the stuff they break. This does not need to involve SRE.

There needs to be permission to be curious and to cooperate. Leaders should value and reward it. In addition, it requires persistent commitment. Don't start skipping the bootcamps. Don't let the people run at 100% utilization so they have time to do such endeavors.

## Personal thoughts
The core of the message resonates well. The story of the designer breaking prod is strong. 
I see participative safety as a cornerstone, that is not mentioned.

>Avoid 100% utilization of people to upkeep tool development, tool development aiming at enabling others, learning and collaboration.

Provocatively formulated
>Having to enforce processes through restrictions comes from organizational dysfunction. Dysfunction as in lack of tooling, monitoring or system understanding of team members.

>Don't react to a rare downtime in a way as if it is going to happen again all the time. Learn from it as team, improve the guardrails. But avoid fear-guidedly setting up big walls.

>Require distributed ownership of prod. You are responsible for your code beyond its deployment. Ensure it is monitored.

>Well functioning engineering teams are difficult to scale, hard to explain, hard to generalize. Probably worth it.

>Avoid brilliant jerks.

## Sparked follow-up questions
How does that work in heavily regulated industries?
Up to which organizational size this work?
If system stability is considered the highest good, I don't think that the suggested team structure and freedom would be applicable in its entirety. 

How can one rate individual performance within such a team? Peer-review? Opinionated manager impression? Does it even matter, just get stuff done and enjoy?

How do you recruit and find members for such organizations? Let them explain in detail how they work/have worked? Avoid hints of arrogance and elitism?

How do you balance the amount of individual breath and efficiency in getting the job done? You can't have everyone know and understand absolutely everything. Open discussion within the team and in frequent 1:1s?

Should sales and customer success be able to directly ping engineers and draw them into rabbit holes? If there is a lack of system understanding, would those recurring requests lead to better documentation?