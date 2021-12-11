# Decentralized Multi-Agent Reinforcement Learning Approach to Reduce the Electricity Consumption and Billing on the Demand Side

The generation and consumption of electricity is one of the most important factors that are currently affecting the climate change. Developing countries are considerable contributing to this issue as well. To help to control the problem, multiple actions could be taken on the demand side of the system. One of the most productive actions that could be taken, it is to know when electricity appliances can be used mainly for activities related with cooking and cleaning. In addition, a context to include underdeveloped nations should be considered since these are commonly left aside. 

This dissertation aims to propose a model using decentralized multi-agent reinforcement learning to take better decisions regarding the usage of electricity, while modeling the appliances considering their purpose and frequency of use, mainly focusing on those for cooking and cleaning, and giving individual suggestion of the turning on or off those appliances; alongside with considering the customer into the system and modeling the decisions regarding the recommendation as a fuzzy system. In addition, it proposes a system to not only include the model in a real world environment, but also to involve the customer in the system, in addition to considering a developing country environment. 

At the end, the investigation suggest to use a model using deep Q-learning for the multi-agent context to suggest when it is a good moment to turn on or off each cooking and cleaning appliance per house. Showing reductions of up to 5.44\% in the total consumption of the environment, which represents a reduction of 154.21 kg CO2 on average per day, and saving up to 12.45 US dollars per month in one of the houses of the simulated environment. In addition, a system to show the performance of the customer alongside with the suggestion of the model is proposed, which gives access to the information not only through a light and responsive web site, but also through SMS. 

The given main notebook shows the implementation used of this project, and gives an example using 25 episodes to gives a clear idea of how the project works, but for the dissertation more episodes were used. In addition, the notebook used to check the data from Pecan Street Dataset is available.

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

### Running the Notebook
The main notebook, called "Main.ipynb", contains all the code used during this project. On it, there are some variables that should be changed in order to use the different implementations. Please follow these steps to run the notebook.
1. Go the "General Execution" section
2. Make sure the relative paths are correctly writen. (It is assumed that there will be a folder "dataset" at the same level of the notebook, and on this, it will be the "15mins" folder from Pecan Street Dataset)
3. The list "houses_ids" contains the IDs of the houses that will be considered as part of the execution.
4. The variable "consider_human_decision" will manage if the Fuzzy System will take part of the execution or not.
5. The variable "consider_model" will manage if the execution will consider the model or not.
6. The variable "episodes" will say how many episodes will run the code
7. The variable "type_mode" will manage if the model coordinator calls the train or test methods of the models
8. The variable "months_to_use" will tell which months should the model use
9. The varialbe "agent_use" will tell the approach to use (Random/Normal, DeepQLearning, QLearning[Q-Table])
10. The variables "overwrite_env_train" and "overwrite_env_test" are boolean variables to control if one wants to use a previously pickle file or to create a new one for train and test, respectively
11. The variables "overwrite_random_model", "overwrite_qlearning_model", "overwrite_deepqlearning_model" will manage if one wants to overwrite previously pickle file from each type of model. This will be used only when the variable "agent_use" points to the same approach.
12. Select "Run All" options from the Run menu.
