# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clusterfuzz/_internal/protos/untrusted_runner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3clusterfuzz/_internal/protos/untrusted_runner.proto\x1a\x19google/protobuf/any.proto\"\x12\n\x10GetStatusRequest\"K\n\x11GetStatusResponse\x12\x10\n\x08revision\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\x04\x12\x10\n\x08\x62ot_name\x18\x03 \x01(\t\"o\n\rProcessResult\x12\x0f\n\x07\x63ommand\x18\x01 \x03(\t\x12\x13\n\x0breturn_code\x18\x02 \x01(\x05\x12\x0e\n\x06output\x18\x03 \x01(\x0c\x12\x15\n\rtime_executed\x18\x04 \x01(\x01\x12\x11\n\ttimed_out\x18\x05 \x01(\x08\"\xb5\x01\n\x12SetupBuildResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x10\n\x08\x61pp_path\x18\x02 \x01(\t\x12\x16\n\x0e\x61pp_path_debug\x18\x03 \x01(\t\x12\x0f\n\x07\x61pp_dir\x18\x04 \x01(\t\x12\x11\n\tbuild_dir\x18\x05 \x01(\t\x12\x11\n\tbuild_url\x18\x06 \x01(\t\x12\x13\n\x0b\x66uzz_target\x18\x07 \x01(\t\x12\x19\n\x11\x66uzz_target_count\x18\x08 \x01(\x05\"\xe9\x01\n\x18SetupRegularBuildRequest\x12\x16\n\x0e\x62\x61se_build_dir\x18\x01 \x01(\t\x12\x10\n\x08revision\x18\x02 \x01(\x03\x12\x11\n\tbuild_url\x18\x03 \x01(\t\x12\x44\n\x0etarget_weights\x18\x04 \x03(\x0b\x32,.SetupRegularBuildRequest.TargetWeightsEntry\x12\x14\n\x0c\x62uild_prefix\x18\x05 \x01(\t\x1a\x34\n\x12TargetWeightsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x90\x02\n\x11RunProcessRequest\x12\x0f\n\x07\x63mdline\x18\x01 \x01(\t\x12!\n\x19\x63urrent_working_directory\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x12\n\nneed_shell\x18\x04 \x01(\x08\x12\x10\n\x08gestures\x18\x05 \x03(\t\x12\x31\n\x08\x65nv_copy\x18\x06 \x03(\x0b\x32\x1f.RunProcessRequest.EnvCopyEntry\x12\x14\n\x0ctestcase_run\x18\x07 \x01(\x08\x12\x17\n\x0fignore_children\x18\x08 \x01(\x08\x1a.\n\x0c\x45nvCopyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"Q\n\x12RunProcessResponse\x12\x13\n\x0breturn_code\x18\x01 \x01(\x05\x12\x16\n\x0e\x65xecution_time\x18\x02 \x01(\x01\x12\x0e\n\x06output\x18\x03 \x01(\t\"\xb5\x01\n\tPopenArgs\x12\x0f\n\x07\x62ufsize\x18\x01 \x01(\x05\x12\x12\n\nexecutable\x18\x02 \x01(\t\x12\r\n\x05shell\x18\x03 \x01(\x08\x12\x0b\n\x03\x63wd\x18\x04 \x01(\t\x12 \n\x03\x65nv\x18\x05 \x03(\x0b\x32\x13.PopenArgs.EnvEntry\x12\x19\n\nenv_is_set\x18\x06 \x01(\x08:\x05\x66\x61lse\x1a*\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf4\x01\n\x11RunAndWaitRequest\x12\x17\n\x0f\x65xecutable_path\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65\x66\x61ult_args\x18\x02 \x03(\t\x12\x17\n\x0f\x61\x64\x64itional_args\x18\x03 \x03(\t\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12\x1d\n\x15terminate_before_kill\x18\x05 \x01(\x08\x12\x1b\n\x13terminate_wait_time\x18\x06 \x01(\x01\x12\x12\n\ninput_data\x18\x07 \x01(\x0c\x12\x1e\n\npopen_args\x18\x08 \x01(\x0b\x32\n.PopenArgs\x12\x16\n\x0emax_stdout_len\x18\t \x01(\r\"4\n\x12RunAndWaitResponse\x12\x1e\n\x06result\x18\x01 \x01(\x0b\x32\x0e.ProcessResult\"(\n\x14\x46indBuildFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"9\n\x15\x46indBuildFileResponse\x12\r\n\x05\x66ound\x18\x01 \x01(\x08\x12\x11\n\tfile_path\x18\x02 \x01(\t\"D\n\x16\x43reateDirectoryRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x1c\n\x14\x63reate_intermediates\x18\x02 \x01(\x08\")\n\x17\x43reateDirectoryResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"8\n\x16RemoveDirectoryRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x10\n\x08recreate\x18\x02 \x01(\x08\")\n\x17RemoveDirectoryResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"\x19\n\tFileChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"$\n\x12\x43opyFileToResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\"#\n\x13\x43opyFileFromRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"w\n\x18UpdateEnvironmentRequest\x12/\n\x03\x65nv\x18\x01 \x03(\x0b\x32\".UpdateEnvironmentRequest.EnvEntry\x1a*\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1b\n\x19UpdateEnvironmentResponse\"\x15\n\x13UpdateSourceRequest\"\x16\n\x14UpdateSourceResponse\"a\n\x1aSymbolizeStacktraceRequest\x12%\n\x1dunsymbolized_crash_stacktrace\x18\x01 \x01(\t\x12\x1c\n\x14\x65nable_inline_frames\x18\x02 \x01(\x08\"<\n\x1bSymbolizeStacktraceResponse\x12\x1d\n\x15symbolized_stacktrace\x18\x01 \x01(\t\"3\n\x10ListFilesRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x11\n\trecursive\x18\x02 \x01(\x08\"\'\n\x11ListFilesResponse\x12\x12\n\nfile_paths\x18\x01 \x03(\t\"%\n\x15GetFuzzTargetsRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"3\n\x16GetFuzzTargetsResponse\x12\x19\n\x11\x66uzz_target_paths\x18\x01 \x03(\t\"\x91\x01\n\x0b\x43orpusCrash\x12\x13\n\x0b\x63rash_state\x18\x01 \x01(\t\x12\x12\n\ncrash_type\x18\x02 \x01(\t\x12\x15\n\rcrash_address\x18\x03 \x01(\t\x12\x18\n\x10\x63rash_stacktrace\x18\x04 \x01(\t\x12\x11\n\tunit_path\x18\x05 \x01(\t\x12\x15\n\rsecurity_flag\x18\x06 \x01(\x08\"\xd8\x01\n\x0c\x43overageInfo\x12\x19\n\x11\x63orpus_size_units\x18\x05 \x01(\x03\x12\x19\n\x11\x63orpus_size_bytes\x18\x06 \x01(\x03\x12\x17\n\x0f\x63orpus_location\x18\x07 \x01(\t\x12\x1e\n\x16\x63orpus_backup_location\x18\x08 \x01(\t\x12\x1d\n\x15quarantine_size_units\x18\t \x01(\x03\x12\x1d\n\x15quarantine_size_bytes\x18\n \x01(\x03\x12\x1b\n\x13quarantine_location\x18\x0b \x01(\t\"p\n\x14\x43rossPollinateFuzzer\x12 \n\x0b\x66uzz_target\x18\x01 \x01(\x0b\x32\x0b.FuzzTarget\x12\x1a\n\x12\x62\x61\x63kup_bucket_name\x18\x02 \x01(\t\x12\x1a\n\x12\x63orpus_engine_name\x18\x03 \x01(\t\"\x9f\x01\n\x12PruneCorpusRequest\x12 \n\x0b\x66uzz_target\x18\x01 \x01(\x0b\x32\x0b.FuzzTarget\x12\x36\n\x17\x63ross_pollinate_fuzzers\x18\x02 \x03(\x0b\x32\x15.CrossPollinateFuzzer\x12\x1d\n\x15last_execution_failed\x18\x04 \x01(\x08\x12\x10\n\x08revision\x18\x05 \x01(\x03\"\xc1\x01\n\x13PruneCorpusResponse\x12$\n\rcoverage_info\x18\x01 \x01(\x0b\x32\r.CoverageInfo\x12\x1d\n\x07\x63rashes\x18\x02 \x03(\x0b\x32\x0c.CorpusCrash\x12\x1a\n\x12\x66uzzer_binary_name\x18\x03 \x01(\t\x12\x10\n\x08revision\x18\x04 \x01(\x03\x12\x37\n\x17\x63ross_pollination_stats\x18\x05 \x01(\x0b\x32\x16.CrossPollinationStats\"\x1b\n\x0bStatRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"\xec\x01\n\x15\x43rossPollinationStats\x12\x1e\n\x16project_qualified_name\x18\x01 \x01(\t\x12\x0f\n\x07sources\x18\x03 \x01(\t\x12\x1b\n\x13initial_corpus_size\x18\x05 \x01(\x05\x12\x13\n\x0b\x63orpus_size\x18\x06 \x01(\x05\x12\x1d\n\x15initial_edge_coverage\x18\x07 \x01(\x05\x12\x15\n\redge_coverage\x18\x08 \x01(\x05\x12 \n\x18initial_feature_coverage\x18\t \x01(\x05\x12\x18\n\x10\x66\x65\x61ture_coverage\x18\n \x01(\x05\"v\n\x0cStatResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0f\n\x07st_mode\x18\x02 \x01(\r\x12\x0f\n\x07st_size\x18\x03 \x01(\x04\x12\x10\n\x08st_atime\x18\x05 \x01(\x01\x12\x10\n\x08st_mtime\x18\x06 \x01(\x01\x12\x10\n\x08st_ctime\x18\x07 \x01(\x01\"+\n)TerminateStaleApplicationInstancesRequest\",\n*TerminateStaleApplicationInstancesResponse\"\x19\n\x17ResetEnvironmentRequest\"\x1a\n\x18ResetEnvironmentResponse\"=\n\nFuzzTarget\x12\x0e\n\x06\x65ngine\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x0e\n\x06\x62inary\x18\x03 \x01(\t\"\xeb\x01\n\x16ProcessTestcaseRequest\x12\x0e\n\x06\x65ngine\x18\x01 \x01(\t\x12\x34\n\toperation\x18\x02 \x01(\x0e\x32!.ProcessTestcaseRequest.Operation\x12\x13\n\x0btarget_name\x18\x03 \x01(\t\x12\x11\n\targuments\x18\x04 \x03(\t\x12\x15\n\rtestcase_path\x18\x05 \x01(\t\x12\x13\n\x0boutput_path\x18\x06 \x01(\t\x12\x0f\n\x07timeout\x18\x07 \x01(\x04\"&\n\tOperation\x12\x0c\n\x08MINIMIZE\x10\x00\x12\x0b\n\x07\x43LEANSE\x10\x01\"d\n\x15\x45ngineReproduceResult\x12\x0f\n\x07\x63ommand\x18\x01 \x03(\t\x12\x13\n\x0breturn_code\x18\x02 \x01(\x03\x12\x15\n\rtime_executed\x18\x03 \x01(\x01\x12\x0e\n\x06output\x18\x04 \x01(\t\"s\n\x11\x45ngineFuzzRequest\x12\x0e\n\x06\x65ngine\x18\x01 \x01(\t\x12\x13\n\x0btarget_name\x18\x02 \x01(\t\x12\x1d\n\x15sync_corpus_directory\x18\x03 \x01(\t\x12\x1a\n\x12testcase_directory\x18\x04 \x01(\t\"a\n\x0b\x45ngineCrash\x12\x12\n\ninput_path\x18\x01 \x01(\t\x12\x12\n\nstacktrace\x18\x02 \x01(\t\x12\x16\n\x0ereproduce_args\x18\x03 \x03(\t\x12\x12\n\ncrash_time\x18\x04 \x01(\x01\"\xd7\x03\n\x12\x45ngineFuzzResponse\x12\x0c\n\x04logs\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x03(\t\x12\x1d\n\x07\x63rashes\x18\x03 \x03(\x0b\x32\x0c.EngineCrash\x12-\n\x05stats\x18\x04 \x03(\x0b\x32\x1e.EngineFuzzResponse.StatsEntry\x12\x15\n\rtime_executed\x18\x05 \x01(\x01\x12@\n\x0f\x66uzzer_metadata\x18\x06 \x03(\x0b\x32\'.EngineFuzzResponse.FuzzerMetadataEntry\x12\x37\n\nstrategies\x18\x07 \x03(\x0b\x32#.EngineFuzzResponse.StrategiesEntry\x1a\x42\n\nStatsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\x1a\x35\n\x13\x46uzzerMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aG\n\x0fStrategiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"x\n\x16\x45ngineReproduceRequest\x12\x0e\n\x06\x65ngine\x18\x01 \x01(\t\x12\x13\n\x0btarget_name\x18\x02 \x01(\t\x12\x15\n\rtestcase_path\x18\x03 \x01(\t\x12\x11\n\targuments\x18\x04 \x03(\t\x12\x0f\n\x07timeout\x18\x05 \x01(\x01\x32\xa1\n\n\x0fUntrustedRunner\x12\x32\n\tGetStatus\x12\x11.GetStatusRequest\x1a\x12.GetStatusResponse\x12\x43\n\x11SetupRegularBuild\x12\x19.SetupRegularBuildRequest\x1a\x13.SetupBuildResponse\x12\x35\n\nRunProcess\x12\x12.RunProcessRequest\x1a\x13.RunProcessResponse\x12\x35\n\nRunAndWait\x12\x12.RunAndWaitRequest\x1a\x13.RunAndWaitResponse\x12\x44\n\x0f\x43reateDirectory\x12\x17.CreateDirectoryRequest\x1a\x18.CreateDirectoryResponse\x12\x44\n\x0fRemoveDirectory\x12\x17.RemoveDirectoryRequest\x1a\x18.RemoveDirectoryResponse\x12\x32\n\tListFiles\x12\x11.ListFilesRequest\x1a\x12.ListFilesResponse\x12/\n\nCopyFileTo\x12\n.FileChunk\x1a\x13.CopyFileToResponse(\x01\x12\x32\n\x0c\x43opyFileFrom\x12\x14.CopyFileFromRequest\x1a\n.FileChunk0\x01\x12#\n\x04Stat\x12\x0c.StatRequest\x1a\r.StatResponse\x12J\n\x11UpdateEnvironment\x12\x19.UpdateEnvironmentRequest\x1a\x1a.UpdateEnvironmentResponse\x12G\n\x10ResetEnvironment\x12\x18.ResetEnvironmentRequest\x1a\x19.ResetEnvironmentResponse\x12;\n\x0cUpdateSource\x12\x14.UpdateSourceRequest\x1a\x15.UpdateSourceResponse\x12P\n\x13SymbolizeStacktrace\x12\x1b.SymbolizeStacktraceRequest\x1a\x1c.SymbolizeStacktraceResponse\x12}\n\"TerminateStaleApplicationInstances\x12*.TerminateStaleApplicationInstancesRequest\x1a+.TerminateStaleApplicationInstancesResponse\x12\x41\n\x0eGetFuzzTargets\x12\x16.GetFuzzTargetsRequest\x1a\x17.GetFuzzTargetsResponse\x12\x38\n\x0bPruneCorpus\x12\x13.PruneCorpusRequest\x1a\x14.PruneCorpusResponse\x12\x42\n\x0fProcessTestcase\x12\x17.ProcessTestcaseRequest\x1a\x16.EngineReproduceResult\x12\x35\n\nEngineFuzz\x12\x12.EngineFuzzRequest\x1a\x13.EngineFuzzResponse\x12\x42\n\x0f\x45ngineReproduce\x12\x17.EngineReproduceRequest\x1a\x16.EngineReproduceResultB%Z#clusterfuzz/protos/untrusted_runner')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'clusterfuzz._internal.protos.untrusted_runner_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z#clusterfuzz/protos/untrusted_runner'
  _SETUPREGULARBUILDREQUEST_TARGETWEIGHTSENTRY._options = None
  _SETUPREGULARBUILDREQUEST_TARGETWEIGHTSENTRY._serialized_options = b'8\001'
  _RUNPROCESSREQUEST_ENVCOPYENTRY._options = None
  _RUNPROCESSREQUEST_ENVCOPYENTRY._serialized_options = b'8\001'
  _POPENARGS_ENVENTRY._options = None
  _POPENARGS_ENVENTRY._serialized_options = b'8\001'
  _UPDATEENVIRONMENTREQUEST_ENVENTRY._options = None
  _UPDATEENVIRONMENTREQUEST_ENVENTRY._serialized_options = b'8\001'
  _ENGINEFUZZRESPONSE_STATSENTRY._options = None
  _ENGINEFUZZRESPONSE_STATSENTRY._serialized_options = b'8\001'
  _ENGINEFUZZRESPONSE_FUZZERMETADATAENTRY._options = None
  _ENGINEFUZZRESPONSE_FUZZERMETADATAENTRY._serialized_options = b'8\001'
  _ENGINEFUZZRESPONSE_STRATEGIESENTRY._options = None
  _ENGINEFUZZRESPONSE_STRATEGIESENTRY._serialized_options = b'8\001'
  _globals['_GETSTATUSREQUEST']._serialized_start=82
  _globals['_GETSTATUSREQUEST']._serialized_end=100
  _globals['_GETSTATUSRESPONSE']._serialized_start=102
  _globals['_GETSTATUSRESPONSE']._serialized_end=177
  _globals['_PROCESSRESULT']._serialized_start=179
  _globals['_PROCESSRESULT']._serialized_end=290
  _globals['_SETUPBUILDRESPONSE']._serialized_start=293
  _globals['_SETUPBUILDRESPONSE']._serialized_end=474
  _globals['_SETUPREGULARBUILDREQUEST']._serialized_start=477
  _globals['_SETUPREGULARBUILDREQUEST']._serialized_end=710
  _globals['_SETUPREGULARBUILDREQUEST_TARGETWEIGHTSENTRY']._serialized_start=658
  _globals['_SETUPREGULARBUILDREQUEST_TARGETWEIGHTSENTRY']._serialized_end=710
  _globals['_RUNPROCESSREQUEST']._serialized_start=713
  _globals['_RUNPROCESSREQUEST']._serialized_end=985
  _globals['_RUNPROCESSREQUEST_ENVCOPYENTRY']._serialized_start=939
  _globals['_RUNPROCESSREQUEST_ENVCOPYENTRY']._serialized_end=985
  _globals['_RUNPROCESSRESPONSE']._serialized_start=987
  _globals['_RUNPROCESSRESPONSE']._serialized_end=1068
  _globals['_POPENARGS']._serialized_start=1071
  _globals['_POPENARGS']._serialized_end=1252
  _globals['_POPENARGS_ENVENTRY']._serialized_start=1210
  _globals['_POPENARGS_ENVENTRY']._serialized_end=1252
  _globals['_RUNANDWAITREQUEST']._serialized_start=1255
  _globals['_RUNANDWAITREQUEST']._serialized_end=1499
  _globals['_RUNANDWAITRESPONSE']._serialized_start=1501
  _globals['_RUNANDWAITRESPONSE']._serialized_end=1553
  _globals['_FINDBUILDFILEREQUEST']._serialized_start=1555
  _globals['_FINDBUILDFILEREQUEST']._serialized_end=1595
  _globals['_FINDBUILDFILERESPONSE']._serialized_start=1597
  _globals['_FINDBUILDFILERESPONSE']._serialized_end=1654
  _globals['_CREATEDIRECTORYREQUEST']._serialized_start=1656
  _globals['_CREATEDIRECTORYREQUEST']._serialized_end=1724
  _globals['_CREATEDIRECTORYRESPONSE']._serialized_start=1726
  _globals['_CREATEDIRECTORYRESPONSE']._serialized_end=1767
  _globals['_REMOVEDIRECTORYREQUEST']._serialized_start=1769
  _globals['_REMOVEDIRECTORYREQUEST']._serialized_end=1825
  _globals['_REMOVEDIRECTORYRESPONSE']._serialized_start=1827
  _globals['_REMOVEDIRECTORYRESPONSE']._serialized_end=1868
  _globals['_FILECHUNK']._serialized_start=1870
  _globals['_FILECHUNK']._serialized_end=1895
  _globals['_COPYFILETORESPONSE']._serialized_start=1897
  _globals['_COPYFILETORESPONSE']._serialized_end=1933
  _globals['_COPYFILEFROMREQUEST']._serialized_start=1935
  _globals['_COPYFILEFROMREQUEST']._serialized_end=1970
  _globals['_UPDATEENVIRONMENTREQUEST']._serialized_start=1972
  _globals['_UPDATEENVIRONMENTREQUEST']._serialized_end=2091
  _globals['_UPDATEENVIRONMENTREQUEST_ENVENTRY']._serialized_start=1210
  _globals['_UPDATEENVIRONMENTREQUEST_ENVENTRY']._serialized_end=1252
  _globals['_UPDATEENVIRONMENTRESPONSE']._serialized_start=2093
  _globals['_UPDATEENVIRONMENTRESPONSE']._serialized_end=2120
  _globals['_UPDATESOURCEREQUEST']._serialized_start=2122
  _globals['_UPDATESOURCEREQUEST']._serialized_end=2143
  _globals['_UPDATESOURCERESPONSE']._serialized_start=2145
  _globals['_UPDATESOURCERESPONSE']._serialized_end=2167
  _globals['_SYMBOLIZESTACKTRACEREQUEST']._serialized_start=2169
  _globals['_SYMBOLIZESTACKTRACEREQUEST']._serialized_end=2266
  _globals['_SYMBOLIZESTACKTRACERESPONSE']._serialized_start=2268
  _globals['_SYMBOLIZESTACKTRACERESPONSE']._serialized_end=2328
  _globals['_LISTFILESREQUEST']._serialized_start=2330
  _globals['_LISTFILESREQUEST']._serialized_end=2381
  _globals['_LISTFILESRESPONSE']._serialized_start=2383
  _globals['_LISTFILESRESPONSE']._serialized_end=2422
  _globals['_GETFUZZTARGETSREQUEST']._serialized_start=2424
  _globals['_GETFUZZTARGETSREQUEST']._serialized_end=2461
  _globals['_GETFUZZTARGETSRESPONSE']._serialized_start=2463
  _globals['_GETFUZZTARGETSRESPONSE']._serialized_end=2514
  _globals['_CORPUSCRASH']._serialized_start=2517
  _globals['_CORPUSCRASH']._serialized_end=2662
  _globals['_COVERAGEINFO']._serialized_start=2665
  _globals['_COVERAGEINFO']._serialized_end=2881
  _globals['_CROSSPOLLINATEFUZZER']._serialized_start=2883
  _globals['_CROSSPOLLINATEFUZZER']._serialized_end=2995
  _globals['_PRUNECORPUSREQUEST']._serialized_start=2998
  _globals['_PRUNECORPUSREQUEST']._serialized_end=3157
  _globals['_PRUNECORPUSRESPONSE']._serialized_start=3160
  _globals['_PRUNECORPUSRESPONSE']._serialized_end=3353
  _globals['_STATREQUEST']._serialized_start=3355
  _globals['_STATREQUEST']._serialized_end=3382
  _globals['_CROSSPOLLINATIONSTATS']._serialized_start=3385
  _globals['_CROSSPOLLINATIONSTATS']._serialized_end=3621
  _globals['_STATRESPONSE']._serialized_start=3623
  _globals['_STATRESPONSE']._serialized_end=3741
  _globals['_TERMINATESTALEAPPLICATIONINSTANCESREQUEST']._serialized_start=3743
  _globals['_TERMINATESTALEAPPLICATIONINSTANCESREQUEST']._serialized_end=3786
  _globals['_TERMINATESTALEAPPLICATIONINSTANCESRESPONSE']._serialized_start=3788
  _globals['_TERMINATESTALEAPPLICATIONINSTANCESRESPONSE']._serialized_end=3832
  _globals['_RESETENVIRONMENTREQUEST']._serialized_start=3834
  _globals['_RESETENVIRONMENTREQUEST']._serialized_end=3859
  _globals['_RESETENVIRONMENTRESPONSE']._serialized_start=3861
  _globals['_RESETENVIRONMENTRESPONSE']._serialized_end=3887
  _globals['_FUZZTARGET']._serialized_start=3889
  _globals['_FUZZTARGET']._serialized_end=3950
  _globals['_PROCESSTESTCASEREQUEST']._serialized_start=3953
  _globals['_PROCESSTESTCASEREQUEST']._serialized_end=4188
  _globals['_PROCESSTESTCASEREQUEST_OPERATION']._serialized_start=4150
  _globals['_PROCESSTESTCASEREQUEST_OPERATION']._serialized_end=4188
  _globals['_ENGINEREPRODUCERESULT']._serialized_start=4190
  _globals['_ENGINEREPRODUCERESULT']._serialized_end=4290
  _globals['_ENGINEFUZZREQUEST']._serialized_start=4292
  _globals['_ENGINEFUZZREQUEST']._serialized_end=4407
  _globals['_ENGINECRASH']._serialized_start=4409
  _globals['_ENGINECRASH']._serialized_end=4506
  _globals['_ENGINEFUZZRESPONSE']._serialized_start=4509
  _globals['_ENGINEFUZZRESPONSE']._serialized_end=4980
  _globals['_ENGINEFUZZRESPONSE_STATSENTRY']._serialized_start=4786
  _globals['_ENGINEFUZZRESPONSE_STATSENTRY']._serialized_end=4852
  _globals['_ENGINEFUZZRESPONSE_FUZZERMETADATAENTRY']._serialized_start=4854
  _globals['_ENGINEFUZZRESPONSE_FUZZERMETADATAENTRY']._serialized_end=4907
  _globals['_ENGINEFUZZRESPONSE_STRATEGIESENTRY']._serialized_start=4909
  _globals['_ENGINEFUZZRESPONSE_STRATEGIESENTRY']._serialized_end=4980
  _globals['_ENGINEREPRODUCEREQUEST']._serialized_start=4982
  _globals['_ENGINEREPRODUCEREQUEST']._serialized_end=5102
  _globals['_UNTRUSTEDRUNNER']._serialized_start=5105
  _globals['_UNTRUSTEDRUNNER']._serialized_end=6418
# @@protoc_insertion_point(module_scope)
