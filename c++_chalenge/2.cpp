#include<bits/stdc++.h>
using namespace std;

// Few global variable which will be used later on.

//Vector of strings to store the input
vector<string> maze;
/* An array which when added to an element respectively,
  gives us all the reacheable nodes from the initial node */
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
/*
  (newX,newY)-> The farthest point from the initial point in a path
   maxL -> The distance of the farthest point from the initial point
*/
int newX,newY,maxL=0,l=0;

// Check if the current position is valid or not
bool valid(int x, int y, int **visited){
  if(x<0 || y <0 || x>=maze.size() || y>=maze[0].size() || maze[x][y]=='#' || visited[x][y])
    return 0;
  return 1;
}

// Below function is used to perform a simple Breadth First Search
void dfs(int x, int y , int **visited , int **yo,bool check,int rows,int cols){
  	if (visited[x][y]) return ;
    /* Below line helps us in detecting the path, and also to keep
     check whether we visited a node or not.                     */
  	visited[x][y] = l+1;
    l++;
    /* Whenever it is max , the path length is stored in maxL and
      the co-ordinates in (newX,newY)->The farthest point from the initial point
      with which we started this function.                                      */
    if(l>maxL){
      maxL = l;
      newX = x;
      newY = y;
      // Store the way in which different points are visited to acheive this maximum length
      for(int i=0;i<rows;i++)
        for(int j=0;j<cols;j++)
          yo[i][j]=visited[i][j];
    }
    // Loop over all the possible paths it can go to from a point recursivly
  	for (int i = 0; i < 4; i++){
  		int modx = dx[i]+x;
      int mody = dy[i]+y;
      if(!valid(modx,mody,visited))
        continue;
      else
        dfs(modx,mody,visited,yo,check,rows,cols);
  	}
    /* Come back , and mark (x,y) unvisited.
       NOTE: Mark the below variable 1 , i.e. visited[x][y] = 1 ,
        when using very big paths , although making it one will not
        gurantee correctness, but does gives us an answer close to maximum.
    */
    visited[x][y]=0;
    /* If check is true, just count the sum of all
       possible lengths of paths */
    if(!check)
      l--;
}

// Function to reset matrix passed to zeros.
void reset_mat(int **matrix,int rows,int cols){
  for(int i=0;i<rows;i++)
    for(int j=0;j<cols;j++)
      matrix[i][j]=0;
}


/* Resets all the Global and Local variables.
   Needs to be called after performing dfs*/
void reset(int **visited,int **ans,int **yo,int rows,int cols){
  reset_mat(visited,rows,cols);
  reset_mat(ans,rows,cols);
  reset_mat(yo,rows,cols);
  maxL=0,l=0;
}

// Function to count all '.' in the maze
void counter(int *count){
  for(int i=0;i<maze.size();i++)
    for(int j=0;j<maze[0].size();j++)
      if(maze[i][j]=='.')
        *count+=1;
}
// Stores the current path in 'ans' variable
void equate(int **ans,int **yo,int rows,int cols,int *path){
  *path=maxL;
  for(int i=0;i<rows;i++)
    for(int j=0;j<cols;j++)
      ans[i][j]=yo[i][j];
}

// Run the programme with command line arguments
int main(int argc, char *argv[]){
  ifstream file(argv[1]);
	string line;
  int i=0,j=0;

  // Read the input file and store it in 'maze'
	while(getline(file, line))
			maze.push_back(line);

  int rows=maze.size(),cols=maze[0].size();
  // Create pointers to dynamically allocate memory
  int **visited,**ans,**yo;
  visited = (int **) malloc(maze.size()* sizeof(int *));
  ans = (int **) malloc(maze.size()* sizeof(int *));
  yo = (int **) malloc(maze.size()* sizeof(int *));
  // Allocating memory
  for(i=0;i<maze.size();i++){
    visited[i] = (int *) malloc(maze[i].size()* sizeof(int));
    ans[i] = (int *) malloc(maze[i].size()* sizeof(int));
    yo[i] = (int *) malloc(maze[i].size()* sizeof(int));
  }
  // Count the number of '.' available
  int count=0;
  counter(&count);
  reset(visited,ans,yo,rows,cols);
  queue< pair<int,int> > points;
  /*
    Find one point belonging to one unique non-connected path.
    Example: (0,1) and (0,4): The path produced from (0,1) never touches (0,4)
              #..#.
              ..#..
              .##..
              #...#
              #.#..
    Collect all such unique points and store them in a queue
                                                           */
  for(i=0;i<rows&&l<count;i++)
    for(j=0;j<cols&&l<count;j++)
      if(valid(i,j,visited)){
        dfs(i,j,visited,yo,true,rows,cols);
        points.push(make_pair(i,j));
/*
              Need to store all the paths to gurantee correctness,
              this takes care of the following types of examples

	     ..##..
	     .##...
	     .#..#.
             .##.##
             .#....
             ..#..#             
 
					*/
      }

  int path=0;
  // Loop through all the unique points collected from above
  while(!points.empty()){

    /* Reset all the global and local initializers
       Apply DepthFirstSearch once to find a leaf on a tree.
       Use the newly obtained (newX,newY) and perform another
       DFS to obtain the diametre of the tree along with the path.
    */
    reset(visited,ans,yo,rows,cols);
    dfs(points.front().first,points.front().second,visited,yo,false,rows,cols);
    reset(visited,ans,yo,rows,cols);
    dfs(newX,newY,visited,yo,false,rows,cols);
    // Store the max length of the path and the path itself.
    if(maxL>path)
      equate(ans,yo,rows,cols,&path);
    // Remove the point after using it
    points.pop();
  }
  // Open a file output.txt to write the output
  freopen ("output.txt","w",stdout);
  // Output the max_len of the path along with the path itself
  printf("%d\n",path);
  for(int i=0;i<rows;i++){
    for (int j=0;j<cols;j++)
      !ans[i][j] ? (printf("%3c",maze[i][j])) : (printf("%3d",ans[i][j]-1));
    printf("\n");
  }
  // Closes and exits
  fclose (stdout);
  // free the memory
  for(i=0;i<maze.size();i++){
    free(visited[i]);
    free(ans[i]);
    free(yo[i]);
  }
  free(visited),free(ans),free(yo);
  return 0;
}
