( ls testsuite/RA/valid/*.ttl ;
  ls testsuite/RA/valid/*.nq ;
  ls testsuite/RA/valid/*.xml ;
  ls testsuite/RA/valid/*.rdf
) \
  | awk '{ print "echo \"Checking file: "$1"\"; scripts/CheckFile.sh "$1; }' \
  | bash
