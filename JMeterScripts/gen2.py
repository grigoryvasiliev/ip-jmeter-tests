sample = '''
		<elementProp name="siteurlnum_1" elementType="Argument">
            <stringProp name="Argument.name">siteurlnum_1</stringProp>
            <stringProp name="Argument.value">http://atperf/sites/toplevelsite0/</stringProp>
            <stringProp name="Argument.metadata">=</stringProp>
        </elementProp>
'''
res = ''


sample2 = '''
<ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group %(num)s" enabled="true">
        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
          <boolProp name="LoopController.continue_forever">false</boolProp>
          <stringProp name="LoopController.loops">-1</stringProp>
        </elementProp>
        <stringProp name="ThreadGroup.num_threads">${users}</stringProp>
        <stringProp name="ThreadGroup.ramp_time">${rampUp}</stringProp>
        <longProp name="ThreadGroup.start_time">1302713373000</longProp>
        <longProp name="ThreadGroup.end_time">1302713373000</longProp>
        <boolProp name="ThreadGroup.scheduler">false</boolProp>
        <stringProp name="ThreadGroup.duration"></stringProp>
        <stringProp name="ThreadGroup.delay"></stringProp>
      </ThreadGroup>
      <hashTree>
        <LoopController guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
          <boolProp name="LoopController.continue_forever">true</boolProp>
          <stringProp name="LoopController.loops">1</stringProp>
        </LoopController>
        <hashTree>
          <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Loading" enabled="true">
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
              <collectionProp name="Arguments.arguments">
                <elementProp name="url" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">${siteurlnum_%(num)s}</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">url</stringProp>
                </elementProp>
                <elementProp name="loading" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">True</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">loading</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
            <stringProp name="HTTPSampler.domain">${server}</stringProp>
            <stringProp name="HTTPSampler.port">3141</stringProp>
            <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.protocol"></stringProp>
            <stringProp name="HTTPSampler.contentEncoding"></stringProp>
            <stringProp name="HTTPSampler.path">/reports/site/permissions</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
            <boolProp name="HTTPSampler.image_parser">true</boolProp>
            <boolProp name="HTTPSampler.monitor">false</boolProp>
            <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          </HTTPSampler2>
          <hashTree>
            <AuthManager guiclass="AuthPanel" testclass="AuthManager" testname="HTTP Authorization Manager" enabled="true">
              <collectionProp name="AuthManager.auth_list">
                <elementProp name="" elementType="Authorization">
                  <stringProp name="Authorization.url">${baseURL}</stringProp>
                  <stringProp name="Authorization.username">${user}</stringProp>
                  <stringProp name="Authorization.password">`1qwerty</stringProp>
                  <stringProp name="Authorization.domain">${domain}</stringProp>
                  <stringProp name="Authorization.realm"></stringProp>
                </elementProp>
              </collectionProp>
            </AuthManager>
            <hashTree/>
          </hashTree>
          <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Cache" enabled="true">
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
              <collectionProp name="Arguments.arguments">
                <elementProp name="url" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">${siteurlnum_%(num)s}</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">url</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
            <stringProp name="HTTPSampler.domain">${server}</stringProp>
            <stringProp name="HTTPSampler.port">3141</stringProp>
            <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.protocol"></stringProp>
            <stringProp name="HTTPSampler.contentEncoding"></stringProp>
            <stringProp name="HTTPSampler.path">/site_permission_report</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
            <boolProp name="HTTPSampler.image_parser">true</boolProp>
            <boolProp name="HTTPSampler.monitor">false</boolProp>
            <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          </HTTPSampler2>
          <hashTree>
            <RegexExtractor guiclass="RegexExtractorGui" testclass="RegexExtractor" testname="get actual_on" enabled="true">
              <stringProp name="RegexExtractor.useHeaders">false</stringProp>
              <stringProp name="RegexExtractor.refname">curr_actual_on_%(num)s</stringProp>
              <stringProp name="RegexExtractor.regex">actual_on=(.+?)&apos; ;</stringProp>
              <stringProp name="RegexExtractor.template">$1$</stringProp>
              <stringProp name="RegexExtractor.default">123</stringProp>
              <stringProp name="RegexExtractor.match_number">1</stringProp>
            </RegexExtractor>
            <hashTree/>
            <AuthManager guiclass="AuthPanel" testclass="AuthManager" testname="HTTP Authorization Manager" enabled="true">
              <collectionProp name="AuthManager.auth_list">
                <elementProp name="" elementType="Authorization">
                  <stringProp name="Authorization.url">${baseURL}</stringProp>
                  <stringProp name="Authorization.username">${user}</stringProp>
                  <stringProp name="Authorization.password">`1qwerty</stringProp>
                  <stringProp name="Authorization.domain">${domain}</stringProp>
                  <stringProp name="Authorization.realm"></stringProp>
                </elementProp>
              </collectionProp>
            </AuthManager>
            <hashTree/>
          </hashTree>
          <TransactionController guiclass="TransactionControllerGui" testclass="TransactionController" testname="Prod" enabled="true">
            <boolProp name="TransactionController.parent">false</boolProp>
          </TransactionController>
          <hashTree>
            <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Site Perm State" enabled="true">
              <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
                <collectionProp name="Arguments.arguments">
                  <elementProp name="url" elementType="HTTPArgument">
                    <boolProp name="HTTPArgument.always_encode">false</boolProp>
                    <stringProp name="Argument.value">${siteurlnum_%(num)s}</stringProp>
                    <stringProp name="Argument.metadata">=</stringProp>
                    <boolProp name="HTTPArgument.use_equals">true</boolProp>
                    <stringProp name="Argument.name">url</stringProp>
                  </elementProp>
                  <elementProp name="with_subsites" elementType="HTTPArgument">
                    <boolProp name="HTTPArgument.always_encode">false</boolProp>
                    <stringProp name="Argument.value">true</stringProp>
                    <stringProp name="Argument.metadata">=</stringProp>
                    <boolProp name="HTTPArgument.use_equals">true</boolProp>
                    <stringProp name="Argument.name">with_subsites</stringProp>
                  </elementProp>
                  <elementProp name="actual_on" elementType="HTTPArgument">
                    <boolProp name="HTTPArgument.always_encode">false</boolProp>
                    <stringProp name="Argument.value">${curr_actual_on_%(num)s}</stringProp>
                    <stringProp name="Argument.metadata">=</stringProp>
                    <boolProp name="HTTPArgument.use_equals">true</boolProp>
                    <stringProp name="Argument.name">actual_on</stringProp>
                  </elementProp>
                </collectionProp>
              </elementProp>
              <stringProp name="HTTPSampler.domain">${server}</stringProp>
              <stringProp name="HTTPSampler.port">3141</stringProp>
              <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
              <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
              <stringProp name="HTTPSampler.protocol"></stringProp>
              <stringProp name="HTTPSampler.contentEncoding"></stringProp>
              <stringProp name="HTTPSampler.path">/site_permission/state/</stringProp>
              <stringProp name="HTTPSampler.method">GET</stringProp>
              <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
              <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
              <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
              <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
              <boolProp name="HTTPSampler.image_parser">true</boolProp>
              <boolProp name="HTTPSampler.monitor">false</boolProp>
              <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
            </HTTPSampler2>
            <hashTree>
              <BSFPostProcessor guiclass="TestBeanGUI" testclass="BSFPostProcessor" testname="check state" enabled="true">
                <stringProp name="filename"></stringProp>
                <stringProp name="parameters"></stringProp>
                <stringProp name="script">eval(&apos;var SearchResponse = &apos; + prev.getResponseDataAsString());
vars.put(&quot;state_busy_%(num)s&quot;, SearchResponse.busy);</stringProp>
                <stringProp name="scriptLanguage">javascript</stringProp>
              </BSFPostProcessor>
              <hashTree/>
              <AuthManager guiclass="AuthPanel" testclass="AuthManager" testname="HTTP Authorization Manager" enabled="true">
                <collectionProp name="AuthManager.auth_list">
                  <elementProp name="" elementType="Authorization">
                    <stringProp name="Authorization.url">${baseURL}</stringProp>
                    <stringProp name="Authorization.username">${user}</stringProp>
                    <stringProp name="Authorization.password">`1qwerty</stringProp>
                    <stringProp name="Authorization.domain">${domain}</stringProp>
                    <stringProp name="Authorization.realm"></stringProp>
                  </elementProp>
                </collectionProp>
              </AuthManager>
              <hashTree/>
            </hashTree>
            <WhileController guiclass="WhileControllerGui" testclass="WhileController" testname="While Controller" enabled="true">
              <stringProp name="WhileController.condition">${state_busy_%(num)s}</stringProp>
            </WhileController>
            <hashTree>
              <ConstantTimer guiclass="ConstantTimerGui" testclass="ConstantTimer" testname="Constant Timer" enabled="true">
                <stringProp name="ConstantTimer.delay">1000</stringProp>
              </ConstantTimer>
              <hashTree/>
              <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Site Perm State" enabled="true">
                <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
                  <collectionProp name="Arguments.arguments">
                    <elementProp name="url" elementType="HTTPArgument">
                      <boolProp name="HTTPArgument.always_encode">false</boolProp>
                      <stringProp name="Argument.value">${siteurlnum_%(num)s}</stringProp>
                      <stringProp name="Argument.metadata">=</stringProp>
                      <boolProp name="HTTPArgument.use_equals">true</boolProp>
                      <stringProp name="Argument.name">url</stringProp>
                    </elementProp>
                    <elementProp name="with_subsites" elementType="HTTPArgument">
                      <boolProp name="HTTPArgument.always_encode">false</boolProp>
                      <stringProp name="Argument.value">true</stringProp>
                      <stringProp name="Argument.metadata">=</stringProp>
                      <boolProp name="HTTPArgument.use_equals">true</boolProp>
                      <stringProp name="Argument.name">with_subsites</stringProp>
                    </elementProp>
                    <elementProp name="actual_on" elementType="HTTPArgument">
                      <boolProp name="HTTPArgument.always_encode">false</boolProp>
                      <stringProp name="Argument.value">${curr_actual_on_%(num)s}</stringProp>
                      <stringProp name="Argument.metadata">=</stringProp>
                      <boolProp name="HTTPArgument.use_equals">true</boolProp>
                      <stringProp name="Argument.name">actual_on</stringProp>
                    </elementProp>
                  </collectionProp>
                </elementProp>
                <stringProp name="HTTPSampler.domain">${server}</stringProp>
                <stringProp name="HTTPSampler.port">3141</stringProp>
                <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
                <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
                <stringProp name="HTTPSampler.protocol"></stringProp>
                <stringProp name="HTTPSampler.contentEncoding"></stringProp>
                <stringProp name="HTTPSampler.path">/site_permission/state/</stringProp>
                <stringProp name="HTTPSampler.method">GET</stringProp>
                <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
                <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
                <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
                <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
                <boolProp name="HTTPSampler.image_parser">true</boolProp>
                <boolProp name="HTTPSampler.monitor">false</boolProp>
                <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
              </HTTPSampler2>
              <hashTree>
                <BSFPostProcessor guiclass="TestBeanGUI" testclass="BSFPostProcessor" testname="check state" enabled="true">
                  <stringProp name="filename"></stringProp>
                  <stringProp name="parameters"></stringProp>
                  <stringProp name="script">eval(&apos;var SearchResponse = &apos; + prev.getResponseDataAsString());
vars.put(&quot;state_busy_%(num)s&quot;, SearchResponse.busy);</stringProp>
                  <stringProp name="scriptLanguage">javascript</stringProp>
                </BSFPostProcessor>
                <hashTree/>
                <AuthManager guiclass="AuthPanel" testclass="AuthManager" testname="HTTP Authorization Manager" enabled="true">
                  <collectionProp name="AuthManager.auth_list">
                    <elementProp name="" elementType="Authorization">
                      <stringProp name="Authorization.url">${baseURL}</stringProp>
                      <stringProp name="Authorization.username">${user}</stringProp>
                      <stringProp name="Authorization.password">`1qwerty</stringProp>
                      <stringProp name="Authorization.domain">${domain}</stringProp>
                      <stringProp name="Authorization.realm"></stringProp>
                    </elementProp>
                  </collectionProp>
                </AuthManager>
                <hashTree/>
              </hashTree>
            </hashTree>
          </hashTree>
          <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Cache 2" enabled="true">
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
              <collectionProp name="Arguments.arguments">
                <elementProp name="url" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">${siteurlnum_%(num)s}</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">url</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
            <stringProp name="HTTPSampler.domain">${server}</stringProp>
            <stringProp name="HTTPSampler.port">3141</stringProp>
            <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.protocol"></stringProp>
            <stringProp name="HTTPSampler.contentEncoding"></stringProp>
            <stringProp name="HTTPSampler.path">/site_permission_report</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
            <boolProp name="HTTPSampler.image_parser">true</boolProp>
            <boolProp name="HTTPSampler.monitor">false</boolProp>
            <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          </HTTPSampler2>
          <hashTree>
            <AuthManager guiclass="AuthPanel" testclass="AuthManager" testname="HTTP Authorization Manager" enabled="true">
              <collectionProp name="AuthManager.auth_list">
                <elementProp name="" elementType="Authorization">
                  <stringProp name="Authorization.url">${baseURL}</stringProp>
                  <stringProp name="Authorization.username">${user}</stringProp>
                  <stringProp name="Authorization.password">`1qwerty</stringProp>
                  <stringProp name="Authorization.domain">${domain}</stringProp>
                  <stringProp name="Authorization.realm"></stringProp>
                </elementProp>
              </collectionProp>
            </AuthManager>
            <hashTree/>
            <RegexExtractor guiclass="RegexExtractorGui" testclass="RegexExtractor" testname="get actual_on" enabled="true">
              <stringProp name="RegexExtractor.useHeaders">false</stringProp>
              <stringProp name="RegexExtractor.refname">curr_actual_on_%(num)s</stringProp>
              <stringProp name="RegexExtractor.regex">actual_on=(.+?)&apos; ;</stringProp>
              <stringProp name="RegexExtractor.template">$1$</stringProp>
              <stringProp name="RegexExtractor.default">123</stringProp>
              <stringProp name="RegexExtractor.match_number">1</stringProp>
            </RegexExtractor>
            <hashTree/>
          </hashTree>
        </hashTree>
		</hashTree>
'''

# for i in range(21,51):
	# res += sample % {} + '\n'

for i in range(50):
	res += sample2 % { 'num': i+1 } + '\n'
	
	
f = open('res1.txt', 'w')
f.write( res )
f.close()
	