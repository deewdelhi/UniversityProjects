import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilesHomeComponent } from './files-home.component';

describe('FilesHomeComponent', () => {
  let component: FilesHomeComponent;
  let fixture: ComponentFixture<FilesHomeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FilesHomeComponent]
    });
    fixture = TestBed.createComponent(FilesHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
