import java.io.*;

public class createF {

	public static void main(String[] args){
		try {
			File file = new File("artists.txt");
			FileReader fr = new FileReader(file);
			BufferedReader bf = new BufferedReader(fr);
			StringBuffer sb = new StringBuffer();
			String line;
			while((line = bf.readLine()) != null){
				File dir = new File(line);
				dir.mkdir();
			}
			fr.close();
		} catch(IOException e){
			e.printStackTrace();
		}
	}
}