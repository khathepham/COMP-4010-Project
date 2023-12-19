
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URL;

import ca.pfv.spmf.algorithms.associationrules.closedrules.AlgoClosedRules_UsingFPClose;
import ca.pfv.spmf.algorithms.associationrules.closedrules.AlgoClosedRules_UsingFPClose_lift;
import ca.pfv.spmf.algorithms.frequentpatterns.apriori_close.AlgoAprioriClose;
import ca.pfv.spmf.algorithms.frequentpatterns.apriori_inverse.AlgoAprioriInverse;
import ca.pfv.spmf.algorithms.frequentpatterns.fpgrowth.AlgoFPClose;
import ca.pfv.spmf.algorithms.frequentpatterns.fpgrowth.AlgoFPClose_inverse;
import ca.pfv.spmf.input.transaction_database_list_integers.TransactionDatabase;
import ca.pfv.spmf.patterns.itemset_array_integers_with_count.Itemsets;

/**
 * Example of how to mine closed association rules from the source code.
 * 
 * @author Philippe Fournier-Viger (Copyright 2008)
 */
public class MainClosedAssociationRulesWithFPClose_inverse_lift_saveToFile {

	public static void main(String[] arg) throws IOException {
		// input and output file paths
		String input = fileToPath(arg[0]);
		String output = arg[5];// ".//output.txt";

		// // the threshold
		// double minsupp = Double.parseDouble(arg[1]);// 0.60;
		// double minconf = Double.parseDouble(arg[3]);// 0.60;

		// // Loading the transaction database
		// TransactionDatabase database = new TransactionDatabase();
		// try {
		// database.loadFile(input);
		// } catch (UnsupportedEncodingException e) {
		// e.printStackTrace();
		// } catch (IOException e) {
		// e.printStackTrace();
		// }

		// // STEP 1: Applying the Charm algorithm to find frequent closed itemsets
		// AlgoFPClose algo = new AlgoFPClose();
		// // Run the algorithm
		// // Note that here we use "null" as output file path because we want to keep
		// the
		// // results into memory instead of saving to a file
		// Itemsets patterns = algo.runAlgorithm(input, null, minsupp);

		// By changing the following lines to some other values
		// it is possible to restrict the number of items in the antecedent and
		// consequent of rules
		int maxConsequentLength = 1500;
		int maxAntecedentLength = 1500;

		// STEP 1: Applying the FP-GROWTH algorithm to find frequent itemsets
		// Note that we set the output file path to null because
		// we want to keep the result in memory instead of saving them
		// to an output file in this example.

		// the thresholds that we will use:
		double minsupp = Double.parseDouble(arg[1]);// 0.001;
		double maxsupp = Double.parseDouble(arg[2]);// 0.61;

		// Loading the transaction database
		TransactionDatabase database = new TransactionDatabase();
		try {
			database.loadFile(input);
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		// STEP 1: Applying the Charm algorithm to find frequent closed itemsets
		AlgoFPClose_inverse algo = new AlgoFPClose_inverse();
		// Run the algorithm
		// Note that here we use "null" as output file path because we want to keep the
		// results into memory instead of saving to a file
		Itemsets patterns = algo.runAlgorithm(input, null, minsupp, maxsupp);
		algo.printStats();
		// Show the CFI-Tree for debugging!
		// System.out.println(algo.cfiTree);
		double minlift = Double.parseDouble(arg[4]);// 0.1;
		double minconf = Double.parseDouble(arg[3]);// 0.50;
		// STEP 2: Generate all rules from the set of frequent itemsets (based on
		// Agrawal & Srikant, 94)
		AlgoClosedRules_UsingFPClose algoClosedRules = new AlgoClosedRules_UsingFPClose();
		algoClosedRules.runAlgorithm(patterns, output, database.size(), minconf,
				minlift, algo.cfiTree);
		algoClosedRules.printStats();

	}

	public static String fileToPath(String filename) throws UnsupportedEncodingException {
		URL url = MainClosedAssociationRulesWithFPClose_inverse_lift_saveToFile.class.getResource(filename);
		return java.net.URLDecoder.decode(url.getPath(), "UTF-8");
	}
}
