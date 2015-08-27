#include <fstream>
#include <bits/stdc++.h>
using namespace std;
int main() {  
  std::ofstream outfile;
  vector <string> lines;
  string line;
  ifstream ip ("asm32.asm");
  if(ip.is_open()){
     while(getline(ip, line)){
        lines.push_back(line);
     }
 }
 else
    cout<<"no open";
ip.close();

for(int i=0;i<(lines).size();i++)
    cout<<lines[i]<<endl;



  outfile.open("asm64.asm", std::ios_base::app);
  outfile << "[bits 64]";
  outfile << "\n"; 
  for(int i=0;i<(lines).size();i++)
  {
     if(lines[i].find(" dd") != std::string::npos){
                lines[i].replace(lines[i].find(" dd"),3, " dq");
            }
            if(lines[i].find("eax") != std::string::npos){
                lines[i].replace(lines[i].find("eax"),3, "rax");
            }
            if(lines[i].find("edi") != std::string::npos){
                lines[i].replace(lines[i].find("edi"),3, "rdi");
            }
            if(lines[i].find("esi") != std::string::npos){
                lines[i].replace(lines[i].find("esi"),3, "rsi");
            }
            if(lines[i].find("edx") != std::string::npos){
                lines[i].replace(lines[i].find("edx"),3, "rdx");
            }
    outfile << lines[i];
    outfile << "\n";

}
  return 0;
}

