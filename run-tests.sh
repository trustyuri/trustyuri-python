echo
echo "----------------------------------"
echo "Testing CheckFile for FA"
echo "The tests below should all SUCCEED"
echo "----------------------------------"
echo

ls testsuite/FA/valid/* \
  | awk '{ print "echo \"Checking file: "$1"\"; scripts/CheckFile.sh "$1; }' \
  | bash


echo
echo "-------------------------------"
echo "Testing CheckFile for FA"
echo "The tests below should all FAIL"
echo "-------------------------------"
echo

ls testsuite/FA/invalid/* \
  | awk '{ print "echo \"Checking file: "$1"\"; scripts/CheckFile.sh "$1; }' \
  | bash


echo
echo "----------------------------------"
echo "Testing ProcessFile for FA"
echo "The tests below should all SUCCEED"
echo "----------------------------------"
echo

ls testsuite/FA/pre/* \
  | xargs -n 1 basename \
  | awk '{ print " \
      echo \"Processing file: testsuite/FA/pre/"$1"\"; \
      rm -rf temp; \
      mkdir temp; \
      cp testsuite/FA/pre/"$1" temp/; \
      scripts/ProcessFile.sh temp/"$1"; \
      N=`ls temp`; \
      if [[ -e \"testsuite/FA/valid/$N\" ]]; then \
        echo Success; \
      else \
        echo FAILURE; \
      fi; \
      rm -r temp; \
    "; }' \
  | bash


echo
echo "----------------------------------"
echo "Testing CheckFile for RA"
echo "The tests below should all SUCCEED"
echo "----------------------------------"
echo
( ls testsuite/RA/valid/*.ttl ;
  ls testsuite/RA/valid/*.nq ;
  ls testsuite/RA/valid/*.xml ;
  ls testsuite/RA/valid/*.rdf
) \
  | awk '{ print "echo \"Checking file: "$1"\"; scripts/CheckFile.sh "$1; }' \
  | bash

echo
echo "-------------------------------"
echo "Testing CheckFile for RA"
echo "The tests below should all FAIL"
echo "-------------------------------"
echo

( ls testsuite/RA/invalid/*.ttl ;
  ls testsuite/RA/invalid/*.nq
) \
  | awk '{ print "echo \"Checking file: "$1"\"; scripts/CheckFile.sh "$1; }' \
  | bash


echo
echo "----------------------------------"
echo "Testing TransformRdf for RA"
echo "The tests below should all SUCCEED"
echo "----------------------------------"
echo

( ls testsuite/RA/pre/*.ttl ;
  ls testsuite/RA/pre/*.nq ;
  ls testsuite/RA/pre/*.xml ;
  ls testsuite/RA/pre/*.rdf
) \
  | xargs -n 1 basename \
  | awk '{ print " \
      echo \"Processing file: testsuite/RA/pre/"$1"\"; \
      rm -rf temp; \
      mkdir temp; \
      cp testsuite/RA/pre/"$1" temp/; \
      cd temp; \
      F=\""$1"\"; \
      B=${F%.*}; \
      ../scripts/TransformRdf.sh "$1" http://trustyuri.net/testsuite/$B; \
      cd ..; \
      N=`ls temp | grep RA`; \
      if [[ -f \"testsuite/RA/valid/$N\" ]]; then \
        echo Success; \
      else \
        echo FAILURE; \
      fi; \
      rm -r temp; \
    "; }' \
  | bash
