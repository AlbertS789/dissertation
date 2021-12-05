# Decentralized Multi-Agent Reinforcement Learning Approach to Reduce the Electricity Consumption and Billing on the Demand Side

The generation and consumption of electricity is one of the most important factors that are currently affecting the climate change. Developing countries are considerable contributing to this issue as well. To help to control the problem, multiple actions could be taken on the demand side of the system. One of the most productive actions that could be taken, it is to know when electricity appliances can be used mainly for activities related with cooking and cleaning. In addition, a context to include underdeveloped nations should be considered since these are commonly left aside. 

This dissertation aims to propose a model using decentralized multi-agent reinforcement learning to take better decisions regarding the usage of electricity, while modeling the appliances considering their purpose and frequency of use, mainly focusing on those for cooking and cleaning, and giving individual suggestion of the turning on or off those appliances; alongside with considering the customer into the system and modeling the decisions regarding the recommendation as a fuzzy system. In addition, it proposes a system to not only include the model in a real world environment, but also to involve the customer in the system, in addition to considering a developing country environment. 

At the end, the investigation suggest to use a model using deep Q-learning for the multi-agent context to suggest when it is a good moment to turn on or off each cooking and cleaning appliance per house. Showing reductions of up to 5.44\% in the total consumption of the environment, which represents a reduction of 154.21 kg CO2 on average per day, and saving up to 12.45 US dollars per month in one of the houses of the simulated environment. In addition, a system to show the performance of the customer alongside with the suggestion of the model is proposed, which gives access to the information not only through a light and responsive web site, but also through SMS. 

The given notebook shows the implementation used of this project, and gives an example using 25 episodes to gives a clear idea of how the project works, but for the dissertation more episodes were used.

### Accessing Pecan Street Dataset
This project uses the Pecan Street Dataset (https://www.pecanstreet.org/dataport/) and their policy restricts the unauthorized share of the documents. Thefore, following there are the step to access to the data used in this investigation. 

1. Go to https://dataport.pecanstreet.org/
2. In type of access, at the right side, select "University"
3. Fill the form 
4. Wait around 1 to 2 days for the staff to respond with the credentials

Once the access is granted
1. Login into the system
2. In the upper right menu, select Data > Residential Data
3. In the table on the screen, at the row identified as "15-minute", download the file named "Austin 15-min (22.4 MB)"
4. Extract the files
