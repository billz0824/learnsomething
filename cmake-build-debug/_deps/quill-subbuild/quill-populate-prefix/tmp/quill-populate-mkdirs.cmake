# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/Users/youranzhu/GitHub/learnsomething/cmake-build-debug/_deps/quill-src"
  "/Users/youranzhu/GitHub/learnsomething/cmake-build-debug/_deps/quill-build"
  "/Users/youranzhu/GitHub/learnsomething/cmake-build-debug/_deps/quill-subbuild/quill-populate-prefix"
  "/Users/youranzhu/GitHub/learnsomething/cmake-build-debug/_deps/quill-subbuild/quill-populate-prefix/tmp"
  "/Users/youranzhu/GitHub/learnsomething/cmake-build-debug/_deps/quill-subbuild/quill-populate-prefix/src/quill-populate-stamp"
  "/Users/youranzhu/GitHub/learnsomething/cmake-build-debug/_deps/quill-subbuild/quill-populate-prefix/src"
  "/Users/youranzhu/GitHub/learnsomething/cmake-build-debug/_deps/quill-subbuild/quill-populate-prefix/src/quill-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/Users/youranzhu/GitHub/learnsomething/cmake-build-debug/_deps/quill-subbuild/quill-populate-prefix/src/quill-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/Users/youranzhu/GitHub/learnsomething/cmake-build-debug/_deps/quill-subbuild/quill-populate-prefix/src/quill-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
