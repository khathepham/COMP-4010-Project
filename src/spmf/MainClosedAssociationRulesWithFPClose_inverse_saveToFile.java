
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URL;

import ca.pfv.spmf.algorithms.associationrules.closedrules.AlgoClosedRules_UsingFPClose;
import ca.pfv.spmf.algorithms.frequentpatterns.apriori_inverse.AlgoAprioriInverse;
import ca.pfv.spmf.algorithms.frequentpatterns.fpgrowth.AlgoFPClose;
import ca.pfv.spmf.input.transaction_database_list_integers.TransactionDatabase;
import ca.pfv.spmf.patterns.itemset_array_integers_with_count.Itemsets;

/**
 * Example of how to mine closed association rules from the source code.
 * 
 * @author Philippe Fournier-Viger (Copyright 2008)
 */
public class MainClosedAssociationRulesWithFPClose_inverse_saveToFile {

	public static void main(String[] arg) throws IOException {
		// input and output file paths
		String input = fileToPath(arg[0]);
		String output = arg[5];// ".//output.txt";

		// the threshold
		int maxConsequentLength = 1500;
		int maxAntecedentLength = 1500;

		// STEP 1: Applying the FP-GROWTH algorithm to find frequent itemsets
		// Note that we set the output file path to null because
		// we want to keep the result in memory instead of saving them
		// to an output file in this example.

		// the thresholds that we will use:
		double minsup = Double.parseDouble(arg[1]);// 0.001;
		double maxsup = Double.parseDouble(arg[2]);// 0.61;

		// Applying the APRIORI-Inverse algorithm to find sporadic itemsets
		AlgoAprioriInverse apriori2 = new AlgoAprioriInverse();
		// apply the algorithm
		Itemsets patterns = apriori2.runAlgorithm(minsup, maxsup, input, null);
		int databaseSize = apriori2.getDatabaseSize();
		apriori2.printStats();

		// Show the CFI-Tree for debugging!
		// System.out.println(algo.cfiTree);
		double minlift = Double.parseDouble(arg[4]);// 0.1;
		double minconf = Double.parseDouble(arg[3]);// 0.50;
		// STEP 2: Generate all rules from the set of frequent itemsets (based on
		// Agrawal & Srikant, 94)
		AlgoClosedRules_UsingFPClose algoClosedRules = new AlgoClosedRules_UsingFPClose();
		algoClosedRules.runAlgorithm(patterns, output, databaseSize, minconf, minlift);
		algoClosedRules.printStats();

	}

	public static String fileToPath(String filename) throws UnsupportedEncodingException {
		URL url = MainClosedAssociationRulesWithFPClose_inverse_saveToFile.class.getResource(filename);
		return java.net.URLDecoder.decode(url.getPath(), "UTF-8");
	}
}
