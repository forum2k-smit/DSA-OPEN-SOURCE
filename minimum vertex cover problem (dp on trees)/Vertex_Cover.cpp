#include<bits/stdc++.h>
using namespace std;
vector<long int> adj[100002];
int dp[100005][2]={-1};
//bool vis[100005]={false};
 
int select(int root,int parent,bool ispcovered)//getting the nodes inside the adj list of 1st node of tree , parent =1, if we take or do not take
{
	if(dp[root][ispcovered]!=-1)
		return dp[root][ispcovered];
		
	int &ret=dp[root][ispcovered];//act as a reference to variable changes made in ret every time will be updated  in dp's respective position
	
	ret=0;//if not taken then base condition
	
	if(ispcovered)
	{
		for(int i=0;i<adj[root].size();i++)
		{
			if(adj[root][i]!=parent)
				ret+=select(adj[root][i],root,false);//same way recusively calling select function to see if the node is not included then what is the case build up(recursive leap of faith)
		}
		
		int r=1;
		for(int j=0;j<adj[root].size();j++)
		{
			if(adj[root][j]!=parent)
				r+=select(adj[root][j],root,true);//same way recusively calling select function to see if the node is included then what is the case build up(recursive leap of faith)
		}
		ret=min(r,ret);//returning minimum because we want minimum number of vertices to be included in our set for vertex cover
	}
	else
	{//if current vertex  of adj. list is not included then we need to include the next one compulsory therefore including next one by passing true in function

		ret=1;
		for(int i=0;i<adj[root].size();i++)
		{
			if(adj[root][i]!=parent)
			ret+=select(adj[root][i],root,true);
		}
	}
	
	return ret;
}
int main()
{
	//ios_base::sync_with_stdio(0);
	 ios_base::sync_with_stdio(false);
    cin.tie(NULL);cout.tie(NULL);
    
    int n,u,v;
    cin>>n;
    
    n-=1;
    while(n--)
    {
    	cin>>u>>v;
    	
    	adj[v].push_back(u);
    	adj[u].push_back(v);
    }
 
 
	memset(dp,-1,sizeof(dp));
	
    int rootincluded=1,rootdiscarded=0;
    
    for(int i=0;i<adj[1].size();i++)
    	rootincluded+=select(adj[1][i],1,true);//as included the root so true
    	
    for(int i=0;i<adj[1].size();i++)
    	rootdiscarded+=select(adj[1][i],1,false);//did not included the root so false;
    	
    cout<<min(rootincluded,rootdiscarded)<<"\n";
} 