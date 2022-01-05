# [The Pragmatic Programmer](https://github.com/askming/Personal-reading/issues/4)

_Started in Nov. 4, 2021_

![image](https://user-images.githubusercontent.com/5671771/140426361-9b465d21-0a0d-4737-9e04-55348f9e67f7.png)

## 1. A Pragmatic Philosophy

- 💡 Tips
  - It’s Your Life
  - You Have Agency
  - Provide Options, Don’t Make Lame Excuses
  - Don’t Live with Broken Windows
  - Be a Catalyst for Change
  - Remember the Big Picture
  - Make Quality a Requirements Issue
  - Invest Regularly in Your Knowledge Portfolio
  - Critically Analyze What You Read and Hear
  - English is Just Another Programming Language
  - It’s Both What You Say and the Way You Say It
  - Build Documentation In, Don’t Bolt It On

- **_Software entropy_,** "software rot" or "technical debt", when disorder increases in software
- **_Stone Soup and Boiled Frogs_**, "start-up fatigue":  You may be in a situation where you know exactly what needs doing and how to do it. The entire system just appears before your eyes—you know it’s right. But ask permission to tackle the whole thing and you’ll be met with delays and blank stares. People will form committees, budgets will need approval, and things will get complicated. Everyone will guard their own resources.
- **_Your Knowledge Portfolio_**
   > An investment in knowledge always pays the best interest. -- Benjamin Franklin
  - "expiring assets": assents whose value diminishes over time
  - Guidelines for investment also apply to building knowledge portfolio
    - Invest regularly
    - Diversify
    - Manage risk
    - Buy low, sell high: Learning an emerging technology before it becomes popular can be just as hard as finding an undervalued stock, but the payoff can be just as rewarding.
    - Review and rebalance
  - Goals
    - Learn at least one new language every year
    - Read a technical book each month
    - Read nontechnical books, too
    - Take classes
    - Participate in local user groups and meetups
    - Experiment with different environments
    - Stay current
  - _**Communicate!**_
      > The meaning of your communication is the response you get

---

*2021-11-09*

## 2. A Pragmatic Approach

- 💡 tips: 
  - Good Design Is Easier to Change Than Bad Design
  - DRY—Don’t Repeat Yourself
  - Make It Easy to Reuse
  - Eliminate Effects Between Unrelated Things
  - There Are No Final Decisions
  - Forgo Following Fads
  - Use Tracer Bullets to Find the Target
  - Prototype to Learn
  - Program Close to the Problem Domain
  - Estimate to Avoid Surprises
  - Iterate the Schedule with the Code
  
- **_The Essence of Good Design_**
  - ETC: easier to change
  - Values are things that help you make decisions: should I do this, or that?
  - What if you have no clue what changes may come up?
    - First, fall back on the ultimate "easy to change" path: try to make what you write replaceable
    - Second, treat this as a way to develop instincts.

- **_DRY—The Evils of Duplication_**
  - DRY principle: _Every piece of knowledge must have a single, unambiguous, authoritative, representation within a system_.
  
- **_Orthogonality_**
  - In computing, the term has come to signify a kind of independence or decoupling. Two or more things are orthogonal if changes in one do not affect any of the others.
  - Two major benefits if you write orthogonal systems: increased productivity and reduced risk.
  - Coding techniques to maintain orthogonality:
    - Keep your code decoupled
    - Avoid global data
    - Avoid similar functions
  - _Refactoring_: Look for any opportunities to reorganize the code to improve its structure and orthogonality.

- **_Tracer Bullets_**
  - Advantages of tracer code approach
    - Users get to see something working early
    - Developers build a structure to work in
    - You have an integration platform
    - You have something to demonstrate
    - You have a better feel for progress
  - Tracer code vs prototyping: Prototyping generates disposable code. Tracer code is lean but complete, and forms part of the skeleton of the final system. Think of prototyping as the reconnaissance and intelligence gathering that takes place before a single tracer bullet is fired.

---

*2022-01-05*

## 3.The Basic Tools

### Power of plain text
- Insurance against obsolescence
- Leverage existing tools
- Easier testing

### Shell games
- A benefit of GUIs is WYSIWYG--what you see is what you get. The disadvantage is WYSIAYG-what you see is all you get.

### Power editing
- In the first edition of this book we recommended using a single editor for everything: code, documentation, memos, system administration, and so on. We've softened that position a little. We're happy for you to use as many editors as you want. We'd just like you to be working toward fluency in each.

### Version control
