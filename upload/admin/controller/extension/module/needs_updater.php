<?php

class ControllerExtensionModuleNeedsUpdater extends Controller
{
    public function index()
    {
        $test = "Hello World";
        var_dump($test);
    }

    private function setLanguage(): array
    {
        $data = array();
        $data['heading_title'] = $this->language->get('heading_title');
        $this->document->setTitle($data['heading_title']);
        return $data;
    }
}
