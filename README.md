# Robustness-of-Kademlia-Performance-to-Churn-Rates
Code for CSCI-GA. 2620 Network And Mobile System Final Project: Robustness of Kademlia Performance to Churn Rates 
# Run Kademlia Code on PeerSim
You need to download jre first to run java environment.

To compile the sources, invoke:
```sh
  make
```
To run the code, invoke:
```sh
  make run
```
# Change Kademlia Simulation Configuration
To change network configuration (e.g., churn rate, network size), see [example.cfg](https://github.com/keruwang/Robustness-of-Kademlia-Performance-to-Churn-Rates/blob/2245c2f45ad45614faf0df88df615ca737208813/example.cfg)
To change Kademlia configuration (e.g., alpha, k), see [src/peersim/kademlia/KademliaCommonConfig.java](https://github.com/keruwang/Robustness-of-Kademlia-Performance-to-Churn-Rates/blob/2245c2f45ad45614faf0df88df615ca737208813/src/peersim/kademlia/KademliaCommonConfig.java)
