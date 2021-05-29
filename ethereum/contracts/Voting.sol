pragma solidity ^0.8.1;

contract Voting {
    address public adminAddress;
    bool public electionOn = false;
    modifier onlyOwner {
        require(msg.sender == adminAddress);
        _;
    }
 
    event voterAdded(string name, string constituency);
    event candidateAdded(string name, string constituency, string symbol);
    // event voteEvent();
    struct Voter {
        // name, id, constituency, canVote 
        string name;
        uint idNo;
        string constituency;
        bool canVote;
        bool exists;
    }
    struct Candidate {
        // name, constituency, noofvotes, address
        string name;
        string constituency;
        string symbol;
        uint noOfVotes;
        bool exists;
    }
    
    Voter[] voters;
    mapping(uint => uint) public ballot; //hash to candidate mapping
    Candidate[] candidates;
    mapping(uint => uint) votersList; // voters id to voter mapping
    
    constructor(){
        adminAddress = msg.sender;
        candidates.push(Candidate("nonce", "nonce", "nonce", 0,  false));
        voters.push(Voter("nonce", 0, "nonce", false, false));
    }
    
    function startElection() public onlyOwner {
        electionOn = true;
    }
    
    function endElection() public onlyOwner {
        electionOn = false;
    }
    // add right to vote facility later
    function createVoter(string memory _name, uint _id, string memory _constituency) public {
        require(!voters[votersList[_id]].exists, "Voter id is already registered!.");
        voters.push(Voter(_name, _id, _constituency, true, true));
        votersList[_id] = voters.length - 1;
        
        emit voterAdded(_name, _constituency);
    } 
    function getVotersList() onlyOwner public view returns(Voter[] memory){
        return voters;
    }
    // handle duplicate candidate problem later
    function createCandidate(string memory _name, string memory _constituency, string memory _symbol) onlyOwner public {
        uint candId =  _generateHash(_name, _constituency, _symbol);
        require(!candidates[ballot[candId]].exists, "Candidate already in ballot list!.");
        candidates.push(Candidate(_name, _constituency, _symbol, 0, true));
        ballot[candId] = candidates.length - 1;
        emit candidateAdded(_name, _constituency, _symbol);
    }
    
    function _generateHash(string memory _name, string memory _constituency, string memory _symbol) public pure returns (uint){
        uint hash = uint(keccak256(abi.encodePacked(_name, _constituency, _symbol)));   
        return hash;
    }
    
    function vote(uint _voterId, string memory _voteTo, string memory _constituency, string memory _symbol) public{
        require(electionOn, "Sorry. The election has ended.");
        require(voters[votersList[_voterId]].exists, "You are not registered to vote.");
        require(voters[votersList[_voterId]].canVote, "Sorry. You already voted.");
        uint candId = _generateHash(_voteTo, _constituency, _symbol);
        require(candidates[ballot[candId]].exists, "Selected candidate not found.");
        require(keccak256(abi.encodePacked(candidates[ballot[candId]].constituency)) == keccak256(abi.encodePacked(voters[votersList[_voterId]].constituency)), "Sorry. You are voting for a candidate who is not in your constituency.");
        candidates[ballot[candId]].noOfVotes++; 
        voters[votersList[_voterId]].canVote = false;
    }
    
    function getElectionResult() public view returns (Candidate[] memory){
        require(!electionOn, "Election has not ended.");
        return candidates;
    }
}