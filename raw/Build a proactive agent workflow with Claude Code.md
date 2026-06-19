---
title: "Build a proactive agent workflow with Claude Code"
source: "https://www.youtube.com/watch?v=eSP7PLTXNy8&t=369s"
author:
  - "[[Claude]]"
published: 2026-05-20
created: 2026-06-19
description: "Routines turn Claude Code into a proactive teammate that reads your repo and opens a PR before you've opened your laptop. You'll see one built end to end, learn the trigger, context, and steering deci"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=eSP7PLTXNy8)

Routines turn Claude Code into a proactive teammate that reads your repo and opens a PR before you've opened your laptop. You'll see one built end to end, learn the trigger, context, and steering decisions behind any routine, and leave one /schedule command away from your first.

## Transcript

**0:19** · Hello everyone. How are you?

**0:22** · Good. Okay, amazing. Welcome to the last workshop session of the day. I hope you've all enjoyed the very first day of code with Claude. Uh my name is Maya.

**0:32** · I'm a member of our applied AI team here in Anthropic. Uh what that means is I spend about half my time developing our own first-party products and features, and the other half of my time helping customers develop their very own products, features, agents on top of our models.

**0:49** · Today, I'm here to talk to you about how to build a proactive agent workflow with Claude Code.

**0:55** · Um can I get a show of hands? Who has used our routines feature inside of Claude Code?

**1:02** · All right, some folks over here.

**1:03** · Awesome, awesome. Um that's what I'm going to be talking about today.

**1:07** · Okay, so first off, a question for the group here.

**1:11** · Who has tried to run Claude Code on a cron?

**1:15** · Can I get a show of hands? Folks, put your hands up high. Awesome, awesome. Um now, keep your hands up if you've enjoyed building all of that infra and maintaining that job.

**1:26** · All right, we have one guy back there.

**1:27** · We have one guy. Thank you. Thank you for your effort. Thank you for your work. Um we felt similar pain internally at Anthropic as we tried to develop uh proactive agents uh that run on Claude Code, uh and we decided to do something about it.

**1:43** · So, we believe that coding agents shouldn't wait for you to press enter to get started.

**1:50** · Right now, Claude Code is a really powerful coding tool, but we want to take Claude Code and turn it into a really powerful coding teammate.

**2:00** · A teammate notices when something breaks and does something about it.

**2:05** · Right now, a tool waits for you to enter your prompt and actually press enter.

**2:11** · So, the goal of today's presentation is to talk about how we have created this feature called routines to take Claude Code from a tool today into the teammate of tomorrow.

**2:26** · So, today we'll be talking about four things.

**2:28** · I'll go through some of the challenges that you folks have felt building proactive agents today.

**2:35** · I'll go through this new feature inside of Claude Code called routines.

**2:39** · We'll go through a real example about how we use routines internally at Anthropic to automate documentation creation.

**2:47** · And then finally, we'll talk about applying routines to your own workflows.

**2:53** · So, I want to talk first through the challenges with building proactive agents today.

**3:00** · We all know it's doable, but I want to talk about what what's a little bit cumbersome with this.

**3:07** · The first thing that's a little bit difficult with building proactive agents today is deciding where these agents should run.

**3:14** · You probably don't want them running on your local machine because if you close your laptop or your laptop dies, your agent session is done.

**3:22** · What that means is you'll need to manage things like hosting, data persistence, and authentication.

**3:29** · Basically, you'll need to build a whole infra stack outside of your prompts, which is doable, but it's a lot of work and there's a lot of boilerplate code there.

**3:39** · The next thing you'll need to do is figure out when to actually kick off these sessions and trigger these agents.

**3:46** · Again, you can build things and build on top of cron, or you can do things like uh post to endpoints that you have to spin up. Um but again, there's there's a lot of infra that you need to build yourself here.

**3:59** · Finally, the challenge with building proactive agents today is sometimes you want to be a human in the loop, but other times you want to be a human out of the loop with these agents. Um right now when you kick off a headless Cloud Code session, it's often hard to figure out what your agent is actually doing in real time. There's no way to watch, steer, bound, or even resume your agent session. It's a It's difficult to do that. Um so we wanted to address each of these three issues um and build routines. Routines is a brand new feature inside of Cloud Code.

**4:33** · It's an automation where you can kick off a remote Cloud Code session by only defining the prompt, what repos you want to connect it to, what connectors it has available to work with, and a trigger.

**4:47** · Cloud Code handles the rest.

**4:52** · So there were three kind of main things we were thinking about as we went ahead and developed this routines feature inside of Cloud Code.

**5:01** · The first thing is that we wanted these agents to be always available.

**5:06** · These agents, these routines run on Cloud Code's managed infrastructure.

**5:11** · And what what's nice with that is that we deal with the hosting, the session state, and the connector all for you.

**5:18** · Nothing depends on your laptop being opened, and we deal uh with all of the Cloud stuff for you, which I think is quite nice.

**5:27** · The next thing is we want these agents to be able to work proactively with customizable triggers.

**5:33** · You might want to kick them off on a time-based schedule, or you might want to work uh event-based. Uh we have the ability to work natively with GitHub events, as well as your own custom events that you can post to um webhooks and endpoints with the event payload as context.

**5:53** · Finally, and the last point that I think is really nice is that these Claude Code sessions that get get launched with these routines are interactive and steerable as if you were launching Claude Code in the terminal.

**6:06** · Every routine is really just a Claude Code session under the hood that you can open, you can watch, follow up on, steer, and resume um from web, CLI, and desktop.

**6:20** · And so, I want to walk you guys through a real use case that uh we use here at Anthropic internally.

**6:27** · So, the question for us and for a member of our engineering team is how can we automate docs creation with routines?

**6:37** · So, just to add a little bit of data behind this, weekly PRs for Claude Code have gone up 200% since the beginning of the new year.

**6:46** · This has been super awesome for our Claude Code engineering team.

**6:51** · Um their productivity is insane. This has been really awesome for you folks because you get new features inside of Claude Code very, very quickly.

**7:01** · The one person that this has not been so awesome for is the one engineer responsible for maintaining our documentation across Claude Code and the agent SDK. And so, when routines launched, she was a super big fan and early adopter. And I want to walk you through how she set up a couple routines to help automate documentation creation for Claude Code and our Claude agent SDK.

**7:24** · So, on my side here, I have the terminal open, and I encourage you all to open your terminal and launch Claude Code.

**7:33** · And inside of the terminal here, I'm able to type what we see on the screen here, /schedule, and actually type in something that Sarah, our documentation uh queen, uh has done to actually set up this routine. So, she went and typed in once a week, "Please review all the new changes merged to main against our documentation repo and create a PR to update docs if you see any changes."

**7:58** · I encourage you folks to think right now, what are some tasks that you do every day that would help if they could run on a schedule or if Claude code could actually initiate these sessions for you.

**8:10** · Um I encourage you to think about that.

**8:13** · After kicking this off inside of Claude code, Claude comes back and prompts me with a couple questions.

**8:19** · It might ask, "Hey Maya, what time every week do you want me to actually kick this off? Or once I create a PR, do you want me to notify you in any way? Maybe ping you on Slack?"

**8:29** · And once I answer these questions, Claude actually goes ahead and creates a routine that we'll view in a little bit inside of Claude code on the web.

**8:40** · But first, I want to walk through the three main decisions you'll need to make as you create any routine. The first decision is you'll need to figure out when your routine should trigger.

**8:51** · What's actually the event or is there a certain cadence that you want this to run?

**8:57** · The second decision is what context or what information does Claude need to have to actually be successful here?

**9:04** · Do you need access to certain docs or does Claude need access to certain tools to ping you?

**9:11** · Finally, the last thing to think about is how do you actually steer Claude in the session to keep it honest?

**9:17** · How do you guide Claude Claude to the output that you want? And so, we'll dive into each one of these and I'll talk through how Sarah, a member of our team, actually does this to automate documentation creation.

**9:31** · So, the first one is the trigger.

**9:34** · When should this event actually run?

**9:38** · So, inside of routines, there's basically two ways to do this.

**9:41** · You can have things kick off on a schedule, on a time-based trigger.

**9:46** · For that earlier example I showed you, uh this is how we do a weekly review of differences between our source code for Claude code as well as our documentation repo.

**9:58** · You can also have routines kick off uh on an event-based cadence. So, maybe every time a release is cut, uh you can diff the release branch against the docs and see if there's any new features that you'll need to spin up PRs for in our documentation repo.

**10:14** · Or maybe your engineers actually deploying uh changes and creating PRs might tag their changes. Maybe this is like a new feature. They could tag it with a label that says need docs, and you could actually kick off Claude code sessions anytime one of these uh labeled PRs get merged.

**10:35** · The next thing you'll need to think about is context.

**10:38** · What does your agent actually need to know to be successful?

**10:43** · Likely, you'll need to give it access to either one or more code-based repos. So, for this docs example, uh we need to give Claude access to not only our Claude code source code to figure out what new changes exist there, but also our docs repo, right? For Claude to actually create uh new PRs there.

**11:04** · Next, you might want to provide additional context to these sessions.

**11:08** · Uh maybe for this one example, I want Claude to have access to all of our existing marketing briefs. Maybe I want Claude to use similar language and verbiage that we use uh in other marketing materials externally at Anthropic. So, maybe all of this lives inside of Google Drive, and I'll want to give Claude access to these files during the session, so I'll hook up the drive connector.

**11:31** · Or maybe anytime Claude creates a PR, um I'll actually want it to ping me on Slack. Uh so I'll give it access to the Slack connector.

**11:40** · It's important to think about this as you're setting up the routine because whatever context Claude has, that's uh the ceiling of how successful Claude will be.

**11:53** · Finally, the last thing to think about here is steerability.

**11:57** · How do we actually ensure the quality um of Claude's outputs?

**12:03** · There are a couple ways to do this.

**12:05** · Um one thing that I think is quite interesting is to actually invest in agent-on-agent review.

**12:12** · If folks have actually designed multi-agent systems here and have heard of the generator uh critiquer pattern, uh this is something that we've borrowed here.

**12:22** · You can actually set up one routine to go ahead and create uh docs PRs, and you can set up another routine that maybe triggers on that PR's creation, um to actually go ahead and leave comments on the PR before a human actually gets to it.

**12:38** · Another option, we had emphasized it's nice to have a human out of the loop, but sometimes you actually do need to monitor these Claude code sessions and maybe nudge Claude in a different direction.

**12:48** · What's really nice and what I'll show you in a second is that you can actually open Claude code on the web and you can view what's happening inside of a live session as if you would working with Claude in the terminal.

**12:59** · You can ask it questions mid-session.

**13:01** · You can push it in another another direction.

**13:04** · You You can also resume a past routine or a past session and continue the conversation.

**13:12** · Finally, the last thing we do and what I think is quite obvious is that we verify Claude's outputs.

**13:18** · For this documentation example, we actually render the page that or the documentation page that Claude has changed and created, and we confirm those outputs are what we expect.

**13:29** · And so now I'll jump back into that initial routine that we've kicked off here in this demo. Um and we'll jump to the demo slides. Awesome. And so we can see right now I'm in Claude.ai and I can go over to this left side panel and actually kick click on this uh code button.

**13:50** · And I can jump into routines on this left-hand side.

**13:54** · And I can actually click on this routine that I had created earlier.

**14:00** · On the left-hand side here you can see that it's connected to two repositories, our uh mocked up Claude code source code as well as our Claude code documentation.

**14:12** · You can see that this runs every Monday at 10:00 a.m. and it's connected to GitHub as well as Slack.

**14:20** · These instructions here on the right-hand slide side Claude generated for me based on the initial prompt that I pasted in and the questions that I answered.

**14:29** · We can see here that uh this is a a weekly documentation sync uh for our Claude code fork.

**14:38** · And I can actually go ahead and click on a session here.

**14:42** · And I can see that these initial instructions are what uh gets pasted in for the very beginning of this Claude code session.

**14:51** · We can see that Claude has read these instructions and started by looking at the source code repository to see uh any changes, any recent PRs that have been merged, looked at our change log, and compared that to what's inside of the documentation repo.

**15:07** · We can see Claude's actually found some changes here and gone ahead and opened a PR for me.

**15:14** · This is one example where you can kick off a routine on a schedule.

**15:19** · Now I want to show you another example where we can actually kick off a routine uh based on a GitHub event.

**15:27** · So here I've actually created a new routine and I've already filled some of this in.

**15:32** · I want to make another documentation automation routine.

**15:37** · And but this time I want this to actually trigger every time I create a new GitHub issue.

**15:43** · So I pasted in some instructions here basically to investigate the issue that this session triggers on.

**15:50** · Figure out if it's to a documentation gap and then if it is and if you believe that this is a gap, go ahead, open a PR and actually ping me in this channel.

**16:00** · So I've gone ahead and connected our Claude code documentation repo as well as our source code again and I want to show you how I actually set up this trigger.

**16:09** · Like I had mentioned before, there's two different types of triggers, schedule based and event based and within event based triggers, we have native GitHub events supported here as well as the ability to trigger from your own code by sending a post request.

**16:24** · So here I'll create a GitHub event trigger and trigger on issue opens anytime I open an issue inside of this Claude code documentation repo and I want this connected to Slack so I can send me a ping anytime I make a PR as well as our GitHub NCP.

**16:44** · So I will go ahead and create this here and now let's make sure that this is working. So I have a new issue open here that I'm about to create inside of our Claude code docs repo.

**16:56** · So I happen to know that there are a few few tools missing from docs in this new version. So I'm going to go ahead and actually create this.

**17:07** · So I can see here that I've gone ahead and created that and now let's refresh this page.

**17:14** · And we can can actually that a new run has gotten picked up here.

**17:19** · We can see that these initial instructions are the very first prompts.

**17:22** · Um and we can see that this additional context from this issue were passed in as well.

**17:28** · I happen to know that I actually already have another PR open for this. So, let me just guide Claude to stop this session.

**17:36** · I've already made these changes.

**17:45** · And we can see here the ability to actually steer Claude in real time after routine gets kicked off.

**17:53** · Awesome.

**17:54** · Um now, let's come back and talk about the different ways uh that we can use routines to actually automate your challenges as uh developers.

**18:04** · I want to talk through um a couple ways that we could turn common software engineering or developer challenges into routines with Claude Code.

**18:15** · The first one I want to talk through is this deploy verifier. Um maybe you have recently uh just deployed changes to an to a service and you want to make sure that this service is healthy and you shouldn't roll back these changes.

**18:31** · I want to think about this uh in three ways. First, what should my trigger be here?

**18:37** · Second, what context is important to provide to Claude in this routine? And lastly, how do I plan to actually interact or steer this routine to keep Claude honest?

**18:47** · I happen to know that my CD pipeline can post after every deploy.

**18:52** · So, this seems like a pretty good trigger to actually kick off this routine on.

**18:56** · I can actually post to this uh webhook that we support inside of routines, and this can actually kick off my Claude Code session.

**19:05** · In terms of what context I think is important to provide Claude here, I can think of a couple things.

**19:11** · One, it's probably nice to give Claude access to the source code for the service that we reach it recently deployed on.

**19:18** · Next, it's probably important to give Claude access to monitoring tools. Maybe that's DataDog, maybe that's Grafana. I don't know what you folks use, but um likely helpful to give Claude access to these uh monitoring tools.

**19:32** · And maybe if something goes down, I want Claude to alert me. I want Claude to ping me on Slack or send me an email, um or maybe maybe even send me a text using Twilio or something like that.

**19:43** · These are some of the connectors or the tools that I would give Claude access to inside of this session.

**19:49** · In terms of keeping Claude honest or actually steering my session, maybe I'd start by having Claude run an investigation for me and giving me an eventual no-go or no-go decision to actually roll back this change.

**20:03** · I could jump into Claude code on the web and actually view and read Claude's analysis for this session.

**20:10** · Then maybe I can continue to work with Claude if I actually think that this should be rolled back and actually use Claude to help me roll back a change.

**20:19** · Maybe eventually, as I watch Claude work more and more and trust its decisions, I can let Claude roll back the change itself if, based on the monitoring monitoring data it has access to, uh if I deem that that's the right decision.

**20:33** · There are other challenges, like maybe you want to build an on-call investigator, or maybe you're actually a PM and your job is to go through uh a lot a lot of issues inside of your backlog. Maybe that's GitHub issues, maybe that's posts inside of a Slack channel, and maybe you want to kick off a weekly job that actually reads through all of these issues. Um maybe it's kicked off on a time-based trigger, you give it access to GitHub and Slack and wherever your issues live, um and you use Claude to actually help you prioritize and maybe open PRs for the most important issues.

**21:07** · Okay, my final takeaways here.

**21:09** · Uh Proactive agents beat reactive agents.

**21:13** · We want Claude to go from a tool to a teammate.

**21:17** · You can move from an agent that is waiting for you to actually press enter and create a PR to an agent that reacts to problems and opens a PR itself.

**21:29** · We built routines so you don't have to focus on maintaining all of this infra, but instead you can actually concentrate on your domain and process expertise.

**21:39** · This is what routines handle for you.

**21:41** · And finally, I encourage you to get started with routines today.

**21:46** · You're a single {slash} schedule commands inside of Claude code away from creating your very first routine.

**21:54** · Awesome. Thanks so much.