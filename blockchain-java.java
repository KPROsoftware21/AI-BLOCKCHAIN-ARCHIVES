import java.util.ArrayList;
import java.util.List;

public class Blockchain {
    private List<Block> chain;

    public Blockchain() {
        this.chain = new ArrayList<>();
    }

    public void addBlock(String data) {
        Block block = new Block(data);
        chain.add(block);
    }

    public void printBlocks() {
        for (Block block : chain) {
            System.out.println(block.getData());
        }
    }
}
