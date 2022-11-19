## Replication Package

This is the replication package for the paper: The Achilles’ Heel of the Android Mining Sandbox Approach for Malware Identification.

### Abstract

Android is the most popular operating system for the mobile platform, and smartphones’ ubiquitous nature in our daily lives has only made their security an important topic for researchers and practitioners alike. Previous research results have advocated using the Mining Android Sandbox Approach (MAS approach) to identify malicious behavior in repackaged apps, one of the most popular methods to inject malicious behavior into android apps. Nonetheless, these previous studies have drawn their conclusions using a small dataset of 102 pairs of original and repackaged apps, threatening the findings w.r.t. external validity and opening the question of whether or not the MAS approach scales to larger and more diverse datasets. To mitigate these issues, we conduct a new experiment that reproduces the state-of-the-art research that empirically evaluated the MAS approach performance. Our reproduction study uses a dataset that is an order of magnitude larger than the datasets used in previous research (a total of 1203 pairs of apps with a much diverse distribution of malware families, for instance). To our surprise, our experiments revealed that the accuracy rate of the MAS approach for malware identification drops significantly: F1 score drops from 0.89 in the previous dataset to 0.42 in our larger dataset. After an in-depth assessment, we found that the
representative number of malware from the gappusin family explains the higher number of samples for which the MAS approach fails to correctly classify as malware. Our findings open the discussion on the possible blindspots that plague the MAS approach and their accuracy issues when scaled and reveal the need for complementing the MAS approach with other techniques so that it could effectively detect a broader class of malware.

### Malware Dataset

We use a curated dataset of 1203 repackaged apps available in the AndroZoo (https://androzoo.uni.lu/repackaging) repository, and arrange the samples on the following CSV [file](../paper-droidxptrace-results-F55A/appsHash.csv)

[this subtext](../paper-droidxptrace-results-F55A/final-ds.csv)
