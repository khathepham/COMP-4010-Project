
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URL;

import ca.pfv.spmf.algorithms.frequentpatterns.apriori.AlgoApriori;

/**
 * Example of how to use APRIORI algorithm from the source code.
 * 
 * @author Philippe Fournier-Viger (Copyright 2008)
 */
public class MainTestApriori_saveToFile {

	public static void main(String[] arg) throws IOException {

		String input = fileToPath("pokeparse.txt");
		String output = ".//output_apriori.txt"; // the path for saving the frequent itemsets found

		double minsup = Double.parseDouble(arg[0]);// 0.4; // means a minsup of 2 transaction (we used a relative
													// support)

		// Applying the Apriori algorithm
		AlgoApriori algo = new AlgoApriori();

		// Uncomment the following line to set the maximum pattern length (number of
		// items per itemset)
		// algo.setMaximumPatternLength(3);

		algo.runAlgorithm(minsup, input, output);
		algo.printStats();
	}

	public static String fileToPath(String filename) throws UnsupportedEncodingException {
		URL url = MainTestApriori_saveToFile.class.getResource(filename);
		return java.net.URLDecoder.decode(url.getPath(), "UTF-8");
	}
}
