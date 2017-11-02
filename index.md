
# CPU Parallizable Proof of Work Based Cryptocurrency
#### John Lore (jlore) and Richard Zhu (rzhu1) -- November 1st, 2017

###### URL here

###### summary here

### Background
Cryptocurrency is a quickly expanding subsection of computer science, first emerging onto the scene with Bitcoin. The key idea behind blockchain technology is using computation power to find a random number, or "nonce", which once summed with a block, will hash to a number with _n_ trailing zeroes. The user who manages to first discover this nonce will be awarded the block, and a certain amount of bitcoin. However, there are many problems with the current implementation of bitcoin. This has spawned many alternative currencies, each of which attempts to shore up one or more of these aspects. Take for example, IOTA, a cryptocurrency which is aimed at microtransactions. The current implementation of bitcoin is not conducive to microtransactions, due to the fact that the entire system can only process 3-4 transactions per second. Thus, it cannot handle a high volume of transactions, and so IOTA uses a giant graph called "The Tangle", which makes it easy to perform microtransactions [https://iota.org/IOTA\_Whitepaper.pdf]. Ethereum, the second largest cryptocurrency by market capitalization, attempts to improve scalability, and has a limit of about 20 transactions per second. For comparison, Paypal current processes about an average of 200 transactions per second, with peaks on Cyber Monday of 500 transactions per second. VISA is able to handle almost 2000 transactions per second. Clearly, scalability issues need to be addressed if cryptocurrencies are ever meant to be used for meaningful real world transactions rather than just speculation and investment. Current work is in progress to increase this maximum limit to 1 million transactions per second.

Another problem with mined cryptocurrencies has to do with its integrity. One of the major innovations introduced in the whitepaper by Satoshi Nakamoto was blockchain technology. This technology makes it so the currency is not regulated by a central authority, but rather is decentralized and validated by its users. However, with this, there arises a problem know as mining consolidation. If a single entity is able to comprise over 50% of all the mining power in existence, then this entity would theoretically be able to out-mine everyone else, and thus eventually mine farther on the blockchain than everyone else combined. This undermines the integrity of the currency, because everyone else's hard work on their fork of the blockchain would be completely invalidated, and their currency lost and worthless.

### The Challenge
The challenge therefore is to develop a cryptocurrency which has huge scalability potential, but is balanced such that it is extremely difficult for one body to be able to amass a majority of mining power.

Due to the low number of transactions per second possible with bitcoin, the latency of verifying a transaction is very high. At the moment, it takes over an hour for a transaction to be verified. It is our goal to be able to create an algorithm for a cryptocurrency which not only has a high throughput, but also a low latency, and a latency which does not scale as the number of users and transactions increases.

### Resources
We will most likely be starting from an existing alternative coin implementation. We will be using the whitepaper written by Satoshi Nakamoto [https://bitcoin.org/bitcoin.pdf] as a reference for how bitcoin mining works, and what it is capable of. We will be using whitepapers for other cryptocurrencies as well, to determine what capabilities they lack. All the code for popular alternative currencies are open-sourced, and they all have whitepapers published, and easy to access. We don't think that we would be able to benefit especially from special machines.

### Goals
We plan to achieve a working cryptocurrency which is demonstrably parallel among CPUs and is resistant to GPU parallelization. If work goes ahead of schedule, we would like to actually refine this into a usable and minable currency and publish it for use by the general public. If we are unable to accomplish everything we wish, a reasonable fall-back goal is to come up with simply the algorithm behind the cryptocurrency, eliminating all the overhead and increased difficulty of actually implementing the cryptocurrency, and demonstrating that this algorithm is difficult to parallelize among GPUs, but parallelizes well among CPUs.

For our presentation and demo, ideally, if we are able to accomplish our reach goal and deliver a true minable cryptocurrency, we would be able to complete transactions from one user to another, and so we would hopefully be able to demonstrate that, along with a demonstration of a miner validating the transaction.

### Platform
We plan on using C++ as our language of choice. This is because bitcoin and most subsequent cryptocurrencies are written in C++. The reasoning for this is that these cryptocurrencies must be extremely consistent across all platforms, or a fork will happen in the blockchain. Additionally, C++ has great performance, which is preferred in order to maximize the number of transactions per second. Our cryptocurrency will be platform agnostic. It should not matter which system one is using. 

### Schedule

<schedule here>







Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/JohnLore/418coin/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
