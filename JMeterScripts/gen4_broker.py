sample = '''
<ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="SitePerm %s" enabled="true">
        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
          <boolProp name="LoopController.continue_forever">false</boolProp>
          <intProp name="LoopController.loops">-1</intProp>
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
          <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Broker: SitePermissions" enabled="true">
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
              <collectionProp name="Arguments.arguments">
                <elementProp name="with_subsites" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">1</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">with_subsites</stringProp>
                </elementProp>
                <elementProp name="url" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">${siteurlnum_%s}</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">url</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
            <stringProp name="HTTPSampler.domain">${server}</stringProp>
            <stringProp name="HTTPSampler.port">3143</stringProp>
            <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.protocol"></stringProp>
            <stringProp name="HTTPSampler.contentEncoding"></stringProp>
            <stringProp name="HTTPSampler.path">SitePermissions</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
            <boolProp name="HTTPSampler.image_parser">true</boolProp>
            <boolProp name="HTTPSampler.monitor">false</boolProp>
            <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          </HTTPSampler2>
          <hashTree/>
          <DurationAssertion guiclass="DurationAssertionGui" testclass="DurationAssertion" testname="Duration Assertion" enabled="true">
            <stringProp name="DurationAssertion.duration">${responseTimeout}</stringProp>
          </DurationAssertion>
          <hashTree/>
        </hashTree>
      </hashTree>
'''
res = ''

for i in range(50):
	res += sample % (i,i) + '\n'
	
	
f = open('res1.txt', 'w')
f.write( res )
f.close()
	