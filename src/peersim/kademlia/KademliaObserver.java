package peersim.kademlia;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import peersim.config.Configuration;
import peersim.core.CommonState;
import peersim.core.Control;
import peersim.core.Network;
import peersim.util.IncrementalStats;

/**
 * This class implements a simple observer of search time and hop average in finding a node in the network
 * 
 * @author Daniele Furlan, Maurizio Bonani
 * @version 1.0
 */
public class KademliaObserver implements Control {

	/**
	 * keep statistics of the number of hops of every message delivered.
	 */
	public static IncrementalStats hopStore = new IncrementalStats();

	/**
	 * keep statistics of the time every message delivered.
	 */
	public static IncrementalStats timeStore = new IncrementalStats();

	/**
	 * keep statistic of number of message delivered
	 */
	public static IncrementalStats msg_deliv = new IncrementalStats();

	/**
	 * keep statistic of number of find operation
	 */
	public static IncrementalStats find_op = new IncrementalStats();

	public static IncrementalStats msg_send = new IncrementalStats();

	public static IncrementalStats node_dropped = new IncrementalStats();
	public static IncrementalStats rout_count = new IncrementalStats();
	public static IncrementalStats msg_failed = new IncrementalStats();
	public static IncrementalStats msg_request = new IncrementalStats();	
	/** Parameter of the protocol we want to observe */
	private static final String PAR_PROT = "protocol";

	/** Protocol id */
	private int pid;

	/** Prefix to be printed in output */
	private String prefix;

	public KademliaObserver(String prefix) {
		this.prefix = prefix;
		pid = Configuration.getPid(prefix + "." + PAR_PROT);
	}

	/**
	 * print the statistical snapshot of the current situation
	 * 
	 * @return boolean always false
	 */
	public boolean execute() {
		// get the real network size
		int sz = Network.size();
		for (int i = 0; i < Network.size(); i++)
			if (!Network.get(i).isUp())
				sz--;

	double success_rate = msg_deliv.getSum()/msg_send.getSum();
		double dropRate = node_dropped.getSum()/rout_count.getSum();
		String s = String.format("[time=%d]: [N=%d current nodes UP][%f average h][%f success rate][%d msec average l][%d node dropped][%d rout count][%d diff][%f drop rate]", CommonState.getTime(),sz,hopStore.getAverage(),success_rate,(int) timeStore.getAverage(), (int)node_dropped.getSum(), (int)rout_count.getSum(),(int)msg_send.getSum() - (int)msg_deliv.getSum(),dropRate);

		if (CommonState.getTime() == 3600000) {
			// create hop file
			try {
				File f = new File("D:/simulazioni/hopcountNEW.dat"); // " + sz + "
				f.createNewFile();
				BufferedWriter out = new BufferedWriter(new FileWriter(f, true));
				out.write(String.valueOf(hopStore.getAverage()).replace(".", ",") + ";\n");
				out.close();
			} catch (IOException e) {
			}
			// create latency file
			try {
				File f = new File("D:/simulazioni/latencyNEW.dat");
				f.createNewFile();
				BufferedWriter out = new BufferedWriter(new FileWriter(f, true));
				out.write(String.valueOf(timeStore.getAverage()).replace(".", ",") + ";\n");
				out.close();
			} catch (IOException e) {
			}

		}

		System.err.println(s);

		return false;
	}
}
