#include <queue>
using namespace std;

long const MOD = 1000000007;

class SumInLeavesVisitor : public TreeVis {
public:
    
    int result = 0;
    
    int getResult() {
      	//implement this
        return result;
    }
    void visitNode(TreeNode* node) {
      	//implement this
        
    }

    void visitLeaf(TreeLeaf* leaf) {
        this->result += leaf->getValue();
      	//implement this
    }
};


class ProductOfRedNodesVisitor : public TreeVis {
public:
    long result = 1;
    
    int getResult() {
      	//implement this
        return result;
    }

    void visitNode(TreeNode* node) {
      	//implement this
        if (node->getColor()==Color::RED){
            this->result*=node->getValue();
            this->result%=MOD;
        }
    }

    void visitLeaf(TreeLeaf* leaf) {
      	//implement this
        if (leaf->getColor()==Color::RED){
            this->result*=leaf->getValue();
            this->result%=MOD;
        }
    }

};
//The FancyVisitor implementation must return the absolute difference between the sum of values stored in the tree's non-leaf nodes at even depth and the sum of values stored in the tree's green leaf no
class FancyVisitor : public TreeVis {
public:
    int s1 = 0;
    int s2 = 0;
    int getResult() {
      	//implement this
        return abs(s1-s2);
    }

    void visitNode(TreeNode* node) {
      	//implement this
        if (node->getDepth()%2==0) this->s1+=node->getValue();
    }

    void visitLeaf(TreeLeaf* leaf) {
      	//implement this
        if (leaf->getColor()==Color::GREEN) this->s2+=leaf->getValue();
    }
};

Tree* solve()
{
  	//read the tree from STDIN and return its root as a return value of this function
    int n;
    cin>>n;
    int x[n];
    Color c[n];
    for (int i = 0; i < n; ++i){
        cin>>x[i];
    }
    for (int i = 0; i < n; ++i){
        int col;
        cin>>col;
        if (col==0) c[i]=Color::RED;
        else c[i]= Color::GREEN;
    }
    
    vector<int> ngh[n] = {};
    for (int i = 0; i < n-1; ++i){
        int u, v;
        cin>>u>>v;
        ngh[u-1].push_back(v-1);
        ngh[v-1].push_back(u-1);
    }
    
    int parent[n] = {-1};
    
    TreeNode* root = new TreeNode(x[0], c[0], 0);
    
    queue<int> Q_id;
    queue<TreeNode*> Q;
    
    Q_id.push(0);
    Q.push(root);
    
    while (!Q.empty()){
        
        TreeNode *node = Q.front();
        Q.pop();
        
        int id = Q_id.front();
        Q_id.pop();
        
        //add childrens
        for (vector<int>::iterator it = ngh[id].begin(); it != ngh[id].end(); ++it){
                if (*it!=parent[id]){
                    if (ngh[*it].size()>1){//node
                        TreeNode* child = new TreeNode(x[*it], c[*it], node->getDepth()+1);
                        node->addChild(child);
                        Q.push(child);
                        Q_id.push(*it);
                    }
                    else{//leaf
                        TreeLeaf* child = new TreeLeaf(x[*it], c[*it], node->getDepth()+1);
                        node->addChild(child);
                    }
                    parent[*it] = id;
                }
        }
    }
    
    return root;
}
